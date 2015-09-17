import os
import time

def buildInstallMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "APK Installer Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Choose APK"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the selection tool
        print "TODO add selection tool"
        time.sleep(5)
    if(selection == 2):
        pass
