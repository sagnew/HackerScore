import requests
import simplejson
import random


def get_reputation(user_id):
    url = "http://api.stackoverflow.com/1.1/users/"
    r = requests.get(url + user_id)
    return r.json['users'][0]['reputation']
