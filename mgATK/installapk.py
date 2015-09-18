import os
import time
import subprocess

def buildInstallMenu():
    os.system('cls' if os.name == 'nt' else 'clear')
    selection = ''
    print "APK Installer Module for mgAndroidToolkit"
    print "\nOptions:"
    print "1.)Choose APK"
    print "2.)Exit to main menu"
    selection = int(raw_input("Selection #: "))
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
    apkchoice = int(raw_input("APK Selection: "))
    print cmdresult[apkchoice-1] + " was selected."
    begininstall = raw_input("Begin Install (y/N): ")
    if(begininstall.lower() == "y"):
        print "Starting Install please wait."
        print ("adb install " + "data/apk/" + cmdresult[apkchoice-1])
        installcmd = ("adb install " + "data/apk/" + cmdresult[apkchoice-1])
        installresult = subprocess.check_output(installcmd.split())
        print installresult.split('\r\n')
        print "Install Complete"
        time.sleep(5)
        buildInstallMenu()
        #do install like stuff
    elif(begininstall.lower() == "n"):
        print "Stopping installer"
        time.sleep(2)
        buildInstallMenu()
    else:
        print "Invalid Operation."
        time.sleep(2)
        buildInstallMenu()
