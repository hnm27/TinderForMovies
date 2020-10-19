import uuid

from src.common.Database import Database
from src.model.User import User


class Movie(object):

    def __init__(self, title, category, genre, rating, poster, link, _id=None):
        self.rating = rating
        self.poster = poster
        self.title = title
        self.link = link
        self.category = category
        self.genre = genre
        self._id = uuid.uuid4().hex if _id == None else _id

    def json(self):
        return {
            'title': self.title,
            'rating': self.rating,
            'poster': self.poster,
            'link': self.link,
            'category': self.category,
            'genre': self.genre,
            '_id': self._id
        }

    @classmethod
    def get_all_movies(cls):
        movielist = []
        movies = Database.find("movies", {})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    @classmethod
    def get_topmovies(cls):
        movielist=[]
        movies = Database.find("movies", {'category':"topmovies"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    @classmethod
    def get_bollywood(cls):
        movielist=[]
        movies = Database.find("movies", {'category':"bollywood"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    def get_animation(cls):
        movielist=[]
        movies = Database.find("movies", {'genre':"Animation"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    def get_crime(cls):
        movielist=[]
        movies = Database.find("movies", {'genre':"Crime"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    def get_comedy(cls):
        movielist=[]
        movies = Database.find("movies", {'genre':"Comedy"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    def get_action(cls):
        movielist=[]
        movies = Database.find("movies", {'category':"Action"})
        for m in movies:
            movielist.append(cls(**m))
        return movielist

    def save_to_mongo(self):
        Database.insert("movies", self.json())

    @classmethod
    def get_by_id(cls, movie_id):
        movie = Database.find_one("movies", {'_id': movie_id})
        if movie is not None:
            return movie
        else:
            return None

    def add_to_user_favourite(self, user_id):
        user = User.get_by_id(user_id)
        user.addtofavorites(self._id)

    def add_to_user_liked(self, user_id):
        user = User.get_by_id(user_id)
        user.addtoliked(self._id)

    def add_to_user_unliked(self, user_id):
        user = User.get_by_id(user_id)
        user.addtounliked(self._id)

    def add_to_user_unwatched(self, user_id):
        user = User.get_by_id(user_id)
        user.addtounwatched(self._id)

    def movieAI(user_id):
        user = User.get_by_id(user_id)
        movielist = []
        liked = user.getliked()
        unliked = user.getunliked()
        unwatched = user.getunwatched()
        favourites = user.getfavourites()
        print(favourites)
        all = Movie.get_topmovies()
        likedgenre=[]
        likedcategory=[]
        likedids=[]
        unlikedids=[]
        favouriteids=[]
        unwatchedids=[]
        for i in liked:
            likedgenre.append(i["genre"])
            likedcategory.append(i["category"])
            likedids.append(i["_id"])
        for i in unliked:
            unlikedids.append(i["_id"])
        for i in favourites:
            favouriteids.append(i["_id"])
        for i in unwatched:
            unwatchedids.append(i["_id"])

        likedgenre= list(dict.fromkeys(likedgenre))
        likedcategory = list(dict.fromkeys(likedcategory))

        for i in all:
            if i.genre in likedgenre and i.category in likedcategory:
                movielist.append(i)

        for i in all:
            movielist.append(i)

        new_list = []
        for v in movielist:
            if v._id not in favouriteids and v._id not in likedids and v._id not in unlikedids and v._id not in unwatchedids:
                new_list.append(v)

        new_list = list(dict.fromkeys(new_list))
        return new_list




