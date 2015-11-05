#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton && sid'

"""
imdb_gross.py: Get the budget collections of a movie from iMDB (OMDb API does not retrieve that)
using web scraping.
"""

import urllib2
import re

def budgetFinder(imdbID):
    try:
        response = urllib2.urlopen(urllib2.Request("http://www.imdb.com/title/tt" + str(imdbID) + "/business"))
        data = response.read()
        data = re.sub('[\s+]', '', data)
        budget= re.search(r'<h5>Budget</h5>(.*?)\((estimated)', data).group(1)
        return str(budget)

    except:
        return 'N/A'