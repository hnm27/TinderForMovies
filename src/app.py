from imdb import IMDb
from flask import Flask, render_template, request, session, make_response, url_for
from googleapiclient.discovery import build
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
from src.common.Database import Database
from src.model.Movie import Movie
from src.model.User import User
import requests
from bs4 import BeautifulSoup
from werkzeug.utils import redirect
import random
from re import search
from flask_caching import Cache
import random


app = Flask(__name__)
app.secret_key = "Enter Flask app key"
api_key = "Enter Youtube API Key"
youtube = build('youtube', 'v3', developerKey=api_key)
cache=Cache()
app.config['CACHE_TYPE'] = 'simple'
cache.init_app(app)


@app.route('/')
def login_template():
    return render_template('index.html')


@app.route('/register')
def register_template():
    return render_template('register.html')


@app.route('/auth/login', methods=['POST'])
def user_login():
    email = request.form['email']
    password = request.form['password']
    if User.login(email, password):
        session['email'] = email
        return redirect('/profile')
    else:
        session['email'] = None
        return "<h1>Invalid email address or password. Please try again! :( </h1>"


@app.route('/auth/register', methods=['POST'])
def user_register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    check = User.register_user(name, email, password)
    if check:
        session['email'] = email
        return redirect('/profile')
    else:
        return "User already exists"

@cache.cached(timeout=5,key_prefix="topmovies")
def gettopmoviescache():
    return Movie.get_topmovies()

@cache.cached(timeout=5,key_prefix="bollywood")
def getbollycahe():
    return Movie.get_bollywood()

@cache.cached(timeout=5,key_prefix="favourites")
def getfavcache():
    user = User.get_by_email(session['email'])
    userfavourites = user.getfavourites()
    return userfavourites

@cache.cached(timeout=5,key_prefix="liked")
def getlikedcache():
    user = User.get_by_email(session['email'])
    userliked = user.getliked()
    return userliked

@cache.cached(timeout=5,key_prefix="unwatched")
def getunwatchedcache():
    user = User.get_by_email(session['email'])
    userunwatched=user.getunwatched()
    return userunwatched

@app.route('/profile')
def profile():
    user = User.get_by_email(session['email'])
    name = user.name
    movieslist = Movie.movieAI(user._id)
    random.shuffle(movieslist)
    m = movieslist[0]
    return render_template("main.html", name=name, m=m)


@app.route('/addtofavourites/<string:movieid>', methods=['POST'])
def add_to_favourites(movieid):
    user = User.get_by_email(session['email'])
    userfavourites = user.getfavourites()
    for u in userfavourites:
        if u["_id"] == movieid:
            print("already added to favourites")
            return redirect("/profile")
    user.addtofavorites(movieid)
    return redirect("/profile")


@app.route('/addtounwatched/<string:movieid>', methods=['POST'])
def add_to_unwatched(movieid):
    user = User.get_by_email(session['email'])
    userunwatched = user.getunwatched()
    for u in userunwatched:
        if u["_id"] == movieid:
            print("already added to favourites")
            return redirect("/profile")
    user.addtounwatched(movieid)
    return redirect("/profile")


@app.route('/like/<string:movieid>', methods=['POST'])
def likemovie(movieid):
    user = User.get_by_email(session['email'])
    userliked = user.getliked()
    for u in userliked:
        if u["_id"] == movieid:
            print("already added to liked")
            return redirect("/profile")
    user.addtoliked(movieid)
    return redirect("/profile")


@app.route('/unlike/<string:movieid>', methods=['POST'])
def unlike(movieid):
    user = User.get_by_email(session['email'])
    userunliked = user.getunliked()
    for u in userunliked:
        if u["_id"] == movieid:
            print("already added to unliked")
            return redirect("/profile")
    user.addtounliked(movieid)
    return redirect("/profile")


@app.route('/getfavourites')
def getfavourites():
    user = User.get_by_email(session['email'])
    name = user.name
    userfavourites = getfavcache()
    return render_template("favourites.html", movies=userfavourites, name=name)


@app.route('/getliked')
def getliked():
    user = User.get_by_email(session['email'])
    name = user.name
    userliked = getlikedcache()
    return render_template("liked.html", movies=userliked, name=name)


@app.route('/getunwatched')
def getunwatched():
    user = User.get_by_email(session['email'])
    name = user.name
    userunwatched = getunwatchedcache()
    print(userunwatched)
    return render_template("unwatched.html", movies=userunwatched, name=name)


@app.route('/gettopmovies')
def gettopmovies():
    user = User.get_by_email(session['email'])
    movies = Movie.get_topmovies()
    name = user.name
    return render_template("topmovies.html", movies=movies, name=name)


@app.route('/getbollywood')
def getbolly():
    user = User.get_by_email(session['email'])
    name = user.name
    movies = Movie.get_bollywood()
    return render_template("bollywood.html", movies=movies, name=name)


@app.route('/logout')
def logout():
    session['email'] = None
    return render_template("index.html")


@app.route('/search', methods=["POST"])
def getmovies():
    name = User.get_by_email(session['email']).name
    searchlist = []
    query = request.form['search']
    movies = Movie.get_all_movies()
    for m in movies:
        if search(query, m.title):
            print(m.title)
            searchlist.append(m)
    request1 = youtube.search().list(
        part="snippet",
        maxResults=5,
        q=query+"movie trailer",
        topicId="/m/02vxn",
        regionCode="US"
    )
    responselist = request1.execute()
    responselist1 = responselist["items"]
    print(responselist1)

    for response in responselist1:
        try:
            videoId = response["id"]["videoId"]
        except:
            print("something went wrong")
            videoId=None
        title = response["snippet"]["title"]
        poster = response["snippet"]["thumbnails"]["high"]["url"]
        if videoId != None and poster != None and title != None:
            link = "https://www.youtube.com/watch?v=" + videoId
            movie = Movie(title, "search", "search", "", poster, link)
            searchlist.append(movie)
    return render_template("search.html", movies=searchlist, name=name)


if __name__ == '__main__':
    app.run(port=1234)
