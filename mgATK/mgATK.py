#!/usr/bin/env python
import subprocess
import os
import time
import installapk
import uninstallapk
import utility
import lon

def buildMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Welcome to the mgAndroidToolkit V.09171501"
    print "This system will automate some simple functionality for Android Testing\n"
    print "Options: (Not all are functioning yet and just act as placeholders)\n"
    print "1.) Reboot Android (full phone reboot)"
    print "2.) Install APK"
    print "3.) Uninstall APK"
    print "4.) Utilities (Collection of utilities I use often)"
    print "5.) Lair of naughty (use at your own risk.)"
    print "6.) Exit mgATK"
    selection = input("Selection #: ")
    if(selection == 1):
        os.system('cls' if os.name == 'nt' else 'clear')
        print "Pushing reboot. Please wait..."
        cmd = "adb reboot"

        try:
            result = subprocess.check_output(cmd.split())
            print result.split('\r\n')
        except:
            print "Error in running command"
            pass

        print "Returning to menu..."
        time.sleep(5)
        buildMenu()
    elif (selection == 2):
        installapk.buildInstallMenu()
        print "Returning to menu..."
        time.sleep(5)
        buildMenu()
    elif (selection == 3):
        uninstallapk.buildUninstallMenu()
        print "Returning to menu..."
        time.sleep(5)
        buildMenu()
    elif (selection == 4):
        utility.buildUtilityMenu()
        print "Returning to menu..."
        time.sleep(5)
        buildMenu()
    elif (selection == 5):
        lon.buildLoNMenu()
        print "Returning to menu..."
        time.sleep(5)
        buildMenu()
    elif (selection == 6):
        print "Goodbye"
        exit()
    else:
        print "Please make a valid selection."
        time.sleep(2)
        buildInstallMenu()


#cmd = "ls -l"
#s = subprocess.check_output(cmd.split())
#print s.split('\r\n')

def main():
    #setup basic stuff
    #need to check if device is connected.
    buildMenu()

if __name__ == '__main__':
    main()
