#  ----------------------------------------------------------------
#   menu.py
#   Version: 1.0.2
#   Last Updated: August 12, 2022
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

nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")

nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold2')


#  ---------------------------------------------------------------
#  CUSTOM MENUS ::::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

#add a custom dropdown to top menu
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Autocrop', 'nukescripts.autocrop()')

#add a custom gizmo to left menu
myGizmosMenu = nuke.menu('Nodes').addMenu('myGizmos', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Exponential Glow', 'nuke.createNode("NST_Glow_Exponential.gizmo")', icon="myGizmos_icon.png")
myGizmosMenu.addCommand('Vignette', 'nuke.createNode("NST_apVignette")', icon="myGizmos_icon.png")

#  ---------------------------------------------------------------
#  KEYBOARD SHORTCUTS ::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)
#C:\Program Files\Nuke11.3v5\plugins\icons to find built in icons!


