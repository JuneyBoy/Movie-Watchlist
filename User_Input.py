from Data_Retrieve import *
from CSV_Maker import *
from gsheet_updater import *

def user_input():
    movie_title = input("Enter name of movie watched: ")
    date_watched = input("Enter date (month day, year) movie was watched: ")

    movie_data = get_movie_data(movie_title)

    writable_data = []

    writable_data.append(movie_title)
    writable_data.append(date_watched)
    writable_data.append(get_movie_director(movie_data))
    writable_data.append(get_movie_writer(movie_data))
    writable_data.append(get_movie_year(movie_data))
    writable_data.append(get_movie_rating(movie_data))

    file_to_update = input("Do you want to update .csv file or google sheet? (type csv or gs): ")

    if file_to_update == "csv":
        add_movie_to_csv(writable_data)
    elif file_to_update == "gs":
        add_movie_to_sheet(writable_data)
    

user_input()