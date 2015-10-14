#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'dalton childers'

"""
Testing the OMDb API. Edits(error checking and additional
functionality) will be made soon. Comments will be added
during the editing process.
"""
from myemail import *
from populateDB import *     

def main():

    idNum = 1

    while (idNum < 500000):
        stringId = str(idNum).zfill(7)
        print (stringId)
        idNum = idNum + 1
        omdb_id_search(stringId)

    connection.close()
    print("Progress Complete.")
    subject = 'DataBase Populated'
    text = 'The script has finished and the population process should be complete.'
    sendemail(subject,text)


if __name__ == '__main__':
    main()

