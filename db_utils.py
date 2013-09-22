import pymongo
from constants import username, password

connection_uri = 'mongodb://' + username + ':' + password + '@paulo.mongohq.com:10050/GitRumble'

connection = pymongo.Connection(connection_uri)
db = connection.GitRumble
collection = db.sessions

def insert_into_db(user_dict):
    """
    Inserts a user's information into the collection
    """
    #Only insert if the session is not already in the collection
    while not collection.find({"username": user_dict['username']}).count() == 0:
        #TODO: Make an Exception for multiple users
        return

    collection.insert(user_dict)
    return user_dict
