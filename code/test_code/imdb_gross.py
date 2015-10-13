"""
imdb_gross.py: Get the gross collections of a movie from iMDB (OMDb API does not retrieve that)
using web scraping.
"""
import urllib2
import re

movie_id = raw_input("Enter a movie ID: ")
response = urllib2.urlopen(urllib2.Request("http://www.imdb.com/title/tt" + movie_id + "/business"))
data = response.read()
data = re.sub('[\s+]', '', data)
gross = re.search(r'<h5>Gross</h5>(.*?)\((USA)', data).group(1)
print(gross)
