import os
import time
import tablemaker

def buildLoNMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Lair of Naughty Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Build Tables"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Jump to TableMaker
        print "Starting table menu"
        tablemaker.tableMenu()
        time.sleep(5)
    if(selection == 2):
        pass
