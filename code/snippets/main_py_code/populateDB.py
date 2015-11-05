#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton'

import sqlite3
import requests
import json
import time
from boxOfficeFinder import *
from budgetFinder import *
from myemail import *
from requests.exceptions import ConnectionError

# Open the database
connection = sqlite3.connect('film.db')
cursor = connection.cursor()

"""
omdb_search uses the OMDb API to search
IMDb for movie information.
"""
def omdb_id_search(query):
    try:
        r = requests.get("http://www.omdbapi.com/?i=tt" + str(query) + "&plot=full&r=json&tomatoes=true")
        try:
            parsed_movie_data = json.loads(r.text)
            if parsed_movie_data['Response'] == 'False':
                return

            else:
                if parsed_movie_data['Type'] != 'movie':
                    return

                else:

                    parsed_movie_data['BoxOffice'] = boxOfficeFinder(str(query))
                    budget = budgetFinder(str(query))

                    imdbID = parsed_movie_data['imdbID']
                    title = parsed_movie_data['Title']
                    year = parsed_movie_data['Year']
                    rated = parsed_movie_data['Rated']
                    plot = parsed_movie_data['Plot']
                    genre = parsed_movie_data['Genre']
                    runtime = parsed_movie_data['Runtime']
                    released = parsed_movie_data['Released']
                    production = parsed_movie_data['Production']
                    writer = parsed_movie_data['Writer']
                    director = parsed_movie_data['Director']
                    actors = parsed_movie_data['Actors']
                    language = parsed_movie_data['Language']
                    country = parsed_movie_data['Country']
                    boxOffice = parsed_movie_data['BoxOffice']
                    budget = budget
                    metascore = parsed_movie_data['Metascore']
                    imdbRating = parsed_movie_data['imdbRating']
                    imdbVotes = parsed_movie_data['imdbVotes']
                    awards = parsed_movie_data['Awards']


                    cursor.execute('INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                                       (imdbID, title, year, rated, plot, genre, runtime, released, production, writer, director, actors, language, country, boxOffice, budget, metascore, imdbRating, imdbVotes, awards))

                    connection.commit()
                    time.sleep(1)

        except ValueError:
            return

    except ConnectionError:
        time.sleep(5)
        omdb_id_search(query)






