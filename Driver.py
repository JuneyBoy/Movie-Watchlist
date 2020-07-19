import requests
import json

#returns dictionary of info on movie including title, rating, director, etc.
def get_movie_data(movie, key = '9d1be2d5'):
    base_url = "http://www.omdbapi.com/"
    parameters = {'t': movie, 'r': 'json', 'apikey' : key}
    omdb_resps = requests.get(base_url, params = parameters)
    return(omdb_resps.json())

print(get_movie_data("Frozen"))
#This fuction extracts ratings from Rotten Tomatotes, 