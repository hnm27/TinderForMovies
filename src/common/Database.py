import pymongo

client = pymongo.MongoClient(
    "mongodb://humaidmollah27:Hail689801@tindermovies-shard-00-00.vbb56.mongodb.net:27017,tindermovies-shard-00-01.vbb56.mongodb.net:27017,tindermovies-shard-00-02.vbb56.mongodb.net:27017/<dbname>?ssl=true&replicaSet=atlas-t5jnqz-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.get_database("TinderMovies")


class Database(object):

    @staticmethod
    def insert(collection, data):
        db[collection].insert_one(data)

    @staticmethod
    def find(collection, query):
        return db[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return db[collection].find_one(query)

    @staticmethod
    def delete_one(collection, query):
        return db[collection].remove(query)
