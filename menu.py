#  ----------------------------------------------------------------
#   menu.py
#   Version: 1.0.0
#   Last Updated: August 11, 2022
#   Author: Amanda Jayapurna
#  ----------------------------------------------------------------

import nuke
import platform

# Define where nuke directory is on each OS's network.
Win_Dir = 'C:\Users\ajayapurna\.nuke'
MacOSX_Dir = ' '
Linux_Dir = '/home/ajayapurna/.nuke'

# Set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None



