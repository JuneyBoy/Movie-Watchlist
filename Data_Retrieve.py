import requests
import json

#returns dictionary of info on movie including title, rating, director, etc.
def get_movie_data(movie, key = '9d1be2d5'):
    base_url = "http://www.omdbapi.com/"
    parameters = {'t': movie, 'r': 'json', 'apikey' : key}
    omdb_resps = requests.get(base_url, params = parameters)
    return(omdb_resps.json())

#returns Rotten Tomatoes Score
def get_movie_rating(movie_data):
    ratings_lst = []
    for d in movie_data['Ratings']:
        if d['Source'] == 'Rotten Tomatoes':
            ratings_lst.append(int(d['Value'][:-1]))
    if len(ratings_lst) != 0:
        return ratings_lst[0]
    else:
        return "N/A"


#returns Year
def get_movie_year(movie_data):
    return movie_data['Year']

#returns Writer
def get_movie_writer(movie_data):
    #makes list of those who only wrote the screenplay, excluding those who wrote the story or what the story is based on
    writers = [writer for writer in movie_data['Writer'].split(',') if "screenplay" in writer]
    tot = []
    for writer in writers:
        name_pieces = writer.split('(') 
        print(name_pieces)
        del(name_pieces[-1])
        tot.append(name_pieces[0])
    return tot
        

#returns Director
def get_movie_director(movie_data):
    return movie_data['Director']

