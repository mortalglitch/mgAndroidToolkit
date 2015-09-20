import os
import time
import subprocess

def buildUtilityMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Android Utility Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Push Text as Keyboard"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the keyboard tool
        simpleTextPusher()
        time.sleep(5)
    if(selection == 2):
        pass

def simpleTextPusher():
    print "\n\n:Please note: This method of pushing text cannot handle much data"
    print ":I will be releasing a new version soon intended to long data pushes."
    print ":Current limit : 384 characters from my last test."
    print ":Each space counts as two as it translates to %s\n\n"
    rawText = raw_input("Enter text to push: ")
    cleanText = rawText.replace(' ', '%s')
    pushtextcmd = ("adb shell input keyboard text " + '"' + cleanText + '"')
    pushtextresult = subprocess.check_output(pushtextcmd.split())
    print pushtextresult.split('\r\n')
