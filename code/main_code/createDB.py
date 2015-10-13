#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton'

import sqlite3

# Open the database
connection = sqlite3.connect('film.db')
cursor = connection.cursor()
cursor.execute('PRAGMA foreign_keys = ON;') # Enable foreign key support
cursor.execute('DROP TABLE IF EXISTS films;')
connection.commit()

# Create movies table
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS movies;')
cursor.execute("""CREATE TABLE movies
(
    imdbID TEXT PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    year TEXT NOT NULL,
    rated TEXT NOT NULL,
    plot TEXT NOT NULL,
    genre TEXT NOT NULL,
    runtime TEXT NOT NULL,
    released TEXT NOT NULL,
    production TEXT NOT NULL,
    writer TEXT NOT NULL,
    director TEXT NOT NULL,
    actors TEXT NOT NULL,
    language TEXT NOT NULL,
    country TEXT NOT NULL,
    boxOffice TEXT NOT NULL,
    metascore TEXT NOT NULL,
    imdbRating TEXT NOT NULL,
    imdbVotes TEXT NOT NULL,
    awards TEXT NOT NULL,
    UNIQUE (imdbID)
);""")
connection.commit()

# All Done
connection.close()