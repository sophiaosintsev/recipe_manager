__author__ = 'sophiaosintsev'

import urllib2
import json

food2fork_api = '063eb2a5a6b8c34267ec6d69e02571b3'

def search_recipe():
    api_key = food2fork_api
    # url = 'http://food2fork.com/api/search/' + api_key
    url = "http://food2fork.com/api/search?key=" + api_key + "&q=apple%20pie"
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    print data

def get_recipe():
    api_key = food2fork_api
    url = "http://food2fork.com/api/get?key=" + api_key
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)

    print data

search_recipe()