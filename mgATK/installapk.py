import os
import time
import subprocess

def buildInstallMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print "APK Installer Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Choose APK"
    print "2.)Exit to main menu"
    selection = input("Selection #: ")
    if(selection == 1):
        chooseAPK()
        buildInstallMenu()
    elif(selection == 2):
        pass
    else:
        print "Please make a valid selection."
        time.sleep(2)
        buildInstallMenu()

def chooseAPK():
    # Need to write the selection tool
    print "TODO add selection tool"
    cmd = "ls data/apk"
    cmdresult = subprocess.check_output(cmd.split()).splitlines()
    total = 1
    for result in cmdresult:
        print str(total) + ".) " + result
        total += 1
    apkchoice = input("APK Selection: ")
    print cmdresult[apkchoice-1] + " was selected."
    begininstall = input("Begin Install (y/N): ")
