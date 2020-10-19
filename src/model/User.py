import uuid
import json

from flask import session

from src.common.Database import Database
from src.model import Movie
import hashlib,binascii,os


class User(object):
    def __init__(self, name, email, password, _id=None):
        self._id = uuid.uuid4().hex if _id is None else _id
        self.name = name
        self.email = email
        self.password = password


    @classmethod
    def get_by_email(cls, uemail):
        user = Database.find_one("users", {'email': uemail})
        if user is not None:
            return cls(**user)
        else:
            return None

    @classmethod
    def get_by_id(cls, uid):
        user = Database.find_one("users", {'_id': uid})
        return cls(**user)

    def json(self):
        return {
            'name': self.name,
            'email': self.email,
            'password': self.password,
            '_id': self._id
        }

    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def register_user(name, email, password):
        if User.get_by_email(email) is None:
            user = User(name, email, User.hash_password(password))
            Database.insert("users", user.json())
            session['email'] = email
            return True
        else:
            return False

    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password

    @staticmethod
    def login(email, password):
        user = User.get_by_email(email)
        if user is not None:
            if user.email == email and User.verify_password(user.password,password):
                return True
        else:
            return False

    @staticmethod
    def login_session(email):
        session['email'] = email

    def addtofavorites(self, movieid):
        Database.insert("favourites", self.json_usermovie(movieid))

    def addtoliked(self, movieid):
        Database.insert("liked", self.json_usermovie(movieid))

    def addtounwatched(self, movieid):
        Database.insert("unwatched", self.json_usermovie(movieid))

    def addtounliked(self, movieid):
        Database.insert("unliked", self.json_usermovie(movieid))


    def json_usermovie(self, movieid):
        return {
            "user_id": self._id,
            "movie_id": movieid
        }

    def getfavourites(self):
        favouritelist = []
        favourite = Database.find(collection='favourites', query={'user_id': self._id})
        for f in favourite:
            movie = Movie.Movie.get_by_id(f["movie_id"])
            favouritelist.append(movie)
        return favouritelist

    def getliked(self):
        likedlist = []
        liked = Database.find(collection='liked', query={'user_id': self._id})
        for l in liked:
            movie = Movie.Movie.get_by_id(l["movie_id"])
            likedlist.append(movie)
        return likedlist

    def getunliked(self):
        unlikedlist = []
        liked = Database.find(collection='unliked', query={'user_id': self._id})
        for l in liked:
            movie = Movie.Movie.get_by_id(l["movie_id"])
            unlikedlist.append(movie)
        return unlikedlist

    def getunwatched(self):
        unwatchedlist = []
        unwatched = Database.find(collection='unwatched', query={'user_id': self._id})
        for l in unwatched:
            movie = Movie.Movie.get_by_id(l["movie_id"])
            unwatchedlist.append(movie)
        return unwatchedlist




