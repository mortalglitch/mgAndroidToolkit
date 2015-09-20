import os
import time
import subprocess

def buildUtilityMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "Android Utility Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.) Push Text as Keyboard"
    print "2.) Tap target location"
    print "3.) Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        # Need to write the keyboard tool
        simpleTextPusher()
        time.sleep(2)
        buildUtilityMenu()
    if(selection == 2):
        simpleTapper()
        time.sleep(2)
        buildUtilityMenu()
    if(selection == 3):
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

def simpleTapper():
    print "\n\n: This script will tap the screen will tap the screen in a certain area.\n"
    tapX = raw_input("Enter X position: ")
    tapY = raw_input("Enter Y position: ")
    tapcmd = ("adb shell input tap " + tapX + " " + tapY)
    tapcmdresult = subprocess.check_output(tapcmd.split())
    print tapcmdresult.split('\r\n')
