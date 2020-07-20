import csv
from Data_Retrieve import *

columns = ["Title", "Date Watched", "Director", "Screenwriter", "Release Year", "Rotten Tomato Score"]

movie_data = [] 

with open("movie_watchlist.csv", 'w') as file:
    # creating a csv dict writer object  
    writer = csv.DictWriter(file, fieldnames = columns)  
        
    # writing headers (field names)  
    writer.writeheader()



def add_movie(title, date_watched):
    
    movie_data = get_movie_data(title)

    csv_data = []

    csv_data.append(title)
    csv_data.append(date_watched)
    csv_data.append(get_movie_director(movie_data))
    csv_data.append(get_movie_writer(movie_data))
    csv_data.append(get_movie_year(movie_data))
    csv_data.append(get_movie_rating(movie_data))

    with open("movie_watchlist.csv", 'a') as file:
        csvwriter = csv.writer(file)

        csvwriter.writerow(csv_data)


def user_input():
    movie_title = input("Enter name of movie watched: ")
    date_watched = input("Enter date (month day, year) movie was watched: ")

    add_movie(movie_title, date_watched)







