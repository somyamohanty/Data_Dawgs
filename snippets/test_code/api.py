__author__ = 'dalton childers'
"""
Testing the OMDb API. Edits(error checking and additional
functionality) will be made soon. Comments will be added
during the editing process.
"""
import requests
import json

"""
omdb_search uses the OMDb API to search
IMDb for movie information.
"""
def omdb_search(query):
    r = requests.get("http://www.omdbapi.com/?t=" + query + "&y=&plot=full&r=json")
    parsed_movie_data = json.loads(r.text)
    if parsed_movie_data['Type'] != 'movie':
        print ("ERROR: Your request was a " + parsed_movie_data['Type'])
        print ("NOTICE: You must be using a Windows machine.")
    else:
        print parsed_movie_data['Title']
        print parsed_movie_data['Year']
        print parsed_movie_data['Rated']
        print parsed_movie_data['Released']
        print parsed_movie_data['Runtime']
        print parsed_movie_data['Genre']
        print parsed_movie_data['Director']
        print parsed_movie_data['Writer']
        print parsed_movie_data['Actors']
        print parsed_movie_data['Plot']
        print parsed_movie_data['Language']
        print parsed_movie_data['Country']
        print parsed_movie_data['Awards']
        print parsed_movie_data['Poster']
        print parsed_movie_data['Metascore']
        print parsed_movie_data['imdbRating']
        print parsed_movie_data['imdbVotes']
        print parsed_movie_data['Type']

def main():
    query = raw_input("Which movie would you like to search for: ")
    omdb_search(query)

if __name__ == '__main__':
    main()