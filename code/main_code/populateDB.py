#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton'

import sqlite3
import requests
import json
from boxOfficeFinder import *
from myemail import *

# Open the database
connection = sqlite3.connect('film.db')
cursor = connection.cursor()

"""
omdb_search uses the OMDb API to search
IMDb for movie information.
"""
def omdb_id_search(query):
    r = requests.get("http://www.omdbapi.com/?i=tt" + str(query) + "&plot=full&r=json&tomatoes=true")
    try:
        parsed_movie_data = json.loads(r.text)
        if parsed_movie_data['Response'] == 'False':
            return

        else:
            if parsed_movie_data['Type'] != 'movie':
                return

            else:
                if parsed_movie_data['Genre'] == 'Documentary' or parsed_movie_data['Genre'] == 'Adult':
                    return

                else:

                    parsed_movie_data['BoxOffice'] = boxOfficeFinder(str(query))

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
                    metascore = parsed_movie_data['Metascore']
                    imdbRating = parsed_movie_data['imdbRating']
                    imdbVotes = parsed_movie_data['imdbVotes']
                    awards = parsed_movie_data['Awards']


                    cursor.execute('INSERT OR IGNORE INTO movies VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);',
                                       (imdbID, title, year, rated, plot, genre, runtime, released, production, writer, director, actors, language, country, boxOffice, metascore, imdbRating, imdbVotes, awards))

                    connection.commit()

    except ValueError:
        subject = 'JSON Decoding Error'
        text = 'No JSON object could be decoded. The script will carry on.'
        sendemail(subject,text)
        return






