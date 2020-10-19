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
from flask_share import Share

movielist = []
moviesDB = IMDb()
search = moviesDB.get_top250_movies()
search1 = moviesDB.get_top250_indian_movies()
search2 = moviesDB.get_popular100_tv()
search3 =moviesDB.get_bottom100_movies()
for m in search1:
    movielist.append(m.getID())

for i in movielist:
    movieurl = "https://www.imdb.com/title/tt" + i + "/"
    r = requests.get(url=movieurl)
    soup = BeautifulSoup(r.text, 'html.parser')
    try:
        title = soup.find('title')
        ratingValue = soup.find("span", {"itemprop": "ratingValue"})
        image = soup.find("div", {"class": "poster"}).find("img")["src"]
        link = soup.find("div", {"class": "slate"}).find("a")["href"]
        genre = soup.find("div" , {"class": "subtext"}).find("a")
        if link != None and image != None and title != None and ratingValue != None:
            dm = Movie(title.string,"bollywood",genre.text,ratingValue.string,image,"https://www.imdb.com/" + link)
            dm.save_to_mongo()

        print("Image: " + image)
        print("Link: " "https://www.imdb.com/" + link)
        print(title.string)
        print(ratingValue.string)
        print(genre.text)
    except:
        print("Something went wrong")
    else:
        continue
