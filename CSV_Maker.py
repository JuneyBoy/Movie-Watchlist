import csv
from Data_Retrieve import *

columns = ["Title", "Date Watched", "Director", "Screenwriter", "Release Year"]

movie_data = [] 

with open("movie_watchlist.csv", 'w') as file:
    csvwriter = csv.writer(file)

    csvwriter.writerow(columns)



def add_movie(title, date_watched):
    
    movie_data = get_movie_data(title)

    csv_data = []

    csv_data.append(title)
    csv_data.append(date_watched)
    csv_data.append(get_movie_director(movie_data))
    csv_data.append(get_movie_writer(movie_data))
    csv_data.append(get_movie_year(movie_data))

    with open("movie_watchlist.csv", 'a') as file:
        csvwriter = csv.writer(file)

        csvwriter.writerow(csv_data)


add_movie("True Grit", "July 11, 2020")







