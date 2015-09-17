import os
import time

def buildLoNMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Lair of Naughty Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Coming Soon"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the tool
        print "TODO add soon to be created tool"
        time.sleep(5)
    if(selection == 2):
        pass
