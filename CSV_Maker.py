import csv
from os import path


def add_movie_to_csv(movie_data):
    
    if not path.exists("movie_watchlist.csv"):
        columns = ["Title", "Date Watched", "Director", "Screenwriter", "Release Year", "Rotten Tomato Score"]

        with open("movie_watchlist.csv", 'w') as file: 
            writer = csv.DictWriter(file, fieldnames = columns)  
            writer.writeheader()


    with open("movie_watchlist.csv", 'a', newline="") as file:
        csvwriter = csv.writer(file)
        csvwriter.writerow(movie_data)




