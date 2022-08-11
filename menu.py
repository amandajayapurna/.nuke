#  ----------------------------------------------------------------
#   menu.py
#   Version: 1.0.1
#   Last Updated: August 11, 2022
#   Author: Amanda Jayapurna
#  ----------------------------------------------------------------

#  ---------------------------------------------------------------
#  GLOBAL IMPORTS ::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

import nuke
import platform
import nukescripts

# Define where nuke directory is on each OS's network.
Win_Dir = 'C:\Users\ajayapurna\.nuke'
MacOSX_Dir = ' '
Linux_Dir = '/home/ajayapurna/.nuke'

#Auto-set global directory
if platform.system() == "Windows":
	dir = Win_Dir
elif platform.system() == "Darwin":
	dir = MacOSX_Dir
elif platform.system() == "Linux":
	dir = Linux_Dir
else:
	dir = None


#  ---------------------------------------------------------------
#  KNOB DEFAULTS :::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

nuke.knobDefault('Tracker4.shutteroffset', "centered")
nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')

#  ---------------------------------------------------------------
#  CUSTOM MENUS ::::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

#add a custom dropdown to top menu
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

#add a custom gizmo to left menu
myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon=dir+"/icons/myGizmos_icon.png")
myGizmosMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

#  ---------------------------------------------------------------
#  KEYBOARD SHORTCUTS ::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)
#C:\Program Files\Nuke11.3v5\plugins\icons to find built in icons!
