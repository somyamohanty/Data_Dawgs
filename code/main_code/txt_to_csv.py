__author__ = "Siddhant Sutar"

"""
txt_to_csv.py: Converts a .txt file (delimited with tabs) to .csv.
"""

import sys
import csv

outfile = open(sys.argv[1], 'w', newline='', encoding="UTF-8")
wr = csv.writer(output, quoting=csv.QUOTE_ALL)

with open(sys.argv[0], 'r', encoding="UTF-8") as infile:
    for line in infile:
        titles = line.split('\t')
        wr.writerow(titles)

outfile.close()
 
