Currently early work in progress mgAndroidToolkit.
The goal of this will be to design a quick set of utility scripts for
interacting with Android based devices.

Current Requirements:
- ADB (Android Debugging Bridge): This must be set up as a path export or environment variable.
- Python 2.7.6: This is the version I used but it may be compatible with other variants of Python 2
- Currently the attached device will have to have the ADB RSA key accepted prior to use.

Notes:
It's far from complete and I will probably end up rewriting the structure several times.
Initial design will all primarily be based on calling everything from the mgATK.py
once everything is solid there I plan on making each script operate entirely indenpendent of the project structure.

If you have any questions feel free to file an issue and I will attempt to assist.
