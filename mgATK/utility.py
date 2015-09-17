import os
import time

def buildUtilityMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Android Utility Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Push Text as Keyboard"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the keyboard tool
        print "TODO add keyboard tool"
        time.sleep(5)
    if(selection == 2):
        pass
