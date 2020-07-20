import csv
import Data_Retrieve

columns = ["Title", "Date Watched", "Director", "Screenwriter", "Release Year"]

movie_data = [] 

with open("movie_watchlist.csv", 'w') as file:
    csvwriter = csv.writer(file)

    csvwriter.writerow(columns)


