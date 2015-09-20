import os
import time

def buildUninstallMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "APK Uninstaller Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Choose APK"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the removal tool
        print "TODO add removal tool"
        print "Sorry but at this time the uninstaller is incomplete."
        time.sleep(5)
    if(selection == 2):
        pass
