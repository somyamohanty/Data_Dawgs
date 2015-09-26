"""
movies_list_parser.py: Parses the list of iMDB titles obtained from
ftp://ftp.fu-berlin.de/pub/misc/movies/database/movies.list.gz
"""

with open('../data/movies.list', 'r') as fin:
    data = fin.read().splitlines(True)

# Remove the first 15 header lines, TV series (starts with a "), TV movies, and clean up the
# individual lines to include only the movie title and its year.
data = [x.split('\t')[0] + '\n' for x in data[15:-2] if not x.startswith('"') and '(TV)' not in x]

with open('../data/parsed_movies.txt', 'w') as fout:
    fout.writelines(data)
