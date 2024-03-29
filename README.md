# OBS Python Installer
A simple script to install Python 3.6 and Pip for use by OBS to run python scripts
## Usage
Just [download](https://github.com/sugoidogo/obs-python-installer/releases/latest) and run.
# Windows Defender
Windows Defender will see this installer as a trojan and quarantine it, and Smart Screen will warn you that I haven't paid Microsoft's partners to bypass it. My reccomendation is to disable smartscreen and install a different antivirus, but if you already have python installed you can just use the `.py` file directly.
## Support
Support information for all my software is on my [GitHub profile](https://github.com/sugoidogo)
## Why
OBS Studio supports access to most of it's C plugin api via Python, but only via the now unsupported Python 3.6 on Windows, and requires that you manually locate the python folder before you can start using Python scripts. This makes it a hassle to use python scripts with obs, since you'd have to locate the download for the older version of python, install it (possibly screwing up an existing install of a newer version of python needed for other software in the system), and then locate the install folder in the OBS scripting settings. This script rectifies those issues by downloading Python 3.6 Embedded to the user's obs appdata folder, adding pip to ensure scripts can still install dependancies, and inserting the path to the user's settings files. This way the rest of the system isn't affected by the old python installation and obs gets it's own dedicated python interpreter.
