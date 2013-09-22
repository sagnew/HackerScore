import requests
import json
import urllib2
from bs4 import BeautifulSoup


def get_public_contributions(user):
    public_contributions = 0
    url = 'https://github.com/' + user
    usock = urllib2.urlopen(url)
    soup = BeautifulSoup(usock.read())
    x = soup.find_all('span','num')
    x = x[0]
    for items in x:
        numbers = items.split();
        public_contributions = numbers[0]
    return int(public_contributions)

print get_public_contributions("sagnew")
