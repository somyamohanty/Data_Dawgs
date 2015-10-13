"""
movies_list_parser.py: Parses the list of iMDB titles obtained from
ftp://ftp.fu-berlin.de/pub/misc/movies/database/movies.list.gz
"""
# TV: TV movies, V: videos, VG: video games, SUSPENDED: suspended movies, ????: in development
omit_movies = ('(TV)', '(V)', '(VG)', '{{SUSPENDED}}', '(????)')
movie_data = []

with open('../data/movies.list', 'r') as fin:
    data = fin.read().splitlines(True)

# Remove the first 15 header lines, omit non-movies, and include only movie title and year.
for element in data[15:-2]:
    p = element.split('\t')[0]
    if not p.startswith('"') and not p.endswith(omit_movies):
        movie_data.append(p + '\n')

with open('../data/parsed_movies.txt', 'w') as fout:
    fout.writelines(movie_data)
