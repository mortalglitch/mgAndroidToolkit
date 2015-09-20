Currently early work in progress mgAndroidToolkit.

The goal of this will be to design a quick set of utility scripts for
interacting with Android based devices.

The documentation on this is all currently contained within this README with little
formatting. As I add more I will spruce it up a bit and add more individual documentation
for the more advanced scripts.

**USE AT YOUR OWN RISK.**

Current Requirements:
- ADB (Android Debugging Bridge): This must be set up as a path export or environment variable.
- Python 2.7.6: This is the version I used but it may be compatible with other variants of Python 2
- Currently the attached device will have to have the ADB RSA key accepted prior to use.

How-To use various scripts:
- Main Menu (mgATK.py) - from cmd/terminal start at the root directory of the project. You should see /data /mgATK /test /docs /bin README.rst and setup.py. To launch this project in it's current state you will want to be here and run 'python mgATK/mgATK.py' to start the menu.
- APK Installer (installapk.py) - drop an apk into the data/apk/ folder and the script should recognize it. Once recognized the installer should be able to adb push the file over to the Android device.

Utility:
- Push text as keyboard: This script will type to Android as if a keyboard hardware or external was connected. For most common use activate while in a text field.
- Tap target location: This script will have you put in an x and a y coordinate to tap the screen in that location. This can be used should the touch screen stop responding. 

Notes:
It's far from complete and I will probably end up rewriting the structure several times.
Initial design will all primarily be based on calling everything from the mgATK.py
once everything is solid there I plan on making each script operate entirely indenpendent of the project structure.

If you have any questions feel free to file an issue and I will attempt to assist.
