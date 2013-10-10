import urllib
import simplejson
import random


def get_karma(user):
    url = "http://api.thriftdb.com/api.hnsearch.com/users/"
    search = urllib.urlopen(url + user)
    dict = simplejson.loads(search.read())
    if 'karma' in dict.keys():
        return int(dict['karma'])
    else:
        return 0
