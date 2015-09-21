import itertools
import os
import pickle
import sys
import time

"""
Table Maker Module
This system will be used to help generate various tables that are needed for
other scripts of the mgAndroidToolkit.

author: Joshua Neeley
website: omegaraven.com
"""

def tableMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "mgAndroidToolkit Table Maker\n"
    print "Options: "
    print "1.) Generate Simple PIN Table for Bruteforce"
    print "2.) Return to Lair of Naughty"
    print "More coming soon"
    tablechoice = raw_input("Selection #: ")
    if(int(tablechoice) == 1):
        print "\n"
        simplePIN()
        time.sleep(5)
    if(tablechoice == 2):
        pass

def simplePIN():
    print "Input Q to exit."
    simplepinlength = raw_input("How many digits are assumed in the PIN? ")
    if(simplepinlength == 'Q'):
        tableMenu()
    else:
        try:
            val = int(simplepinlength)
        except ValueError:
            print("Please input a valid number.")
            simplePIN()
        pinmaxlength = int(simplepinlength)
        print "Starting PIN generation please wait (this may take a few minutes)"
        print "Based upon the number of digits"
        data = list(itertools.product([0,1,2,3,4,5,6,7,8,9], repeat = pinmaxlength))
        pin_file = open("data/tables/pinlist.p", "wb")
        pickle.dump(data, pin_file)
        pin_file.close()
        print "pinlist.p has been generated in data/tables"
