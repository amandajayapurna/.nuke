#  ----------------------------------------------------------------
#   menu.py
#   Version: 1.0.4
#   Last Updated: August 15, 2022
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

nuke.knobDefault('MotionBlur2D.shutteroffset', "centered")
nuke.knobDefault('MotionBlur3D.shutteroffset', "centered")
nuke.knobDefault('Transform.shutteroffset', "centered")
nuke.knobDefault('TransformMasked.shutteroffset', "centered")
nuke.knobDefault('TimeBlur.shutteroffset', "centered")
nuke.knobDefault('CornerPin2D.shutteroffset', "centered")
nuke.knobDefault('ScanlineRender.shutteroffset', "centered")
nuke.knobDefault('Card3D.shutteroffset', "centered")
nuke.knobDefault('Tracker4.shutteroffset', "centered")

nuke.knobDefault('Tracker4.label', "Motion: [value transform]\nRef Frame: [value reference_frame]")
nuke.addOnUserCreate(lambda:nuke.thisNode()['reference_frame'].setValue(nuke.frame()), nodeClass='Tracker4')
nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold2')

#  ---------------------------------------------------------------
#  PYTHON :::::::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

import shuffleShortcuts

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

#add custom shuffle node to Channels menu
#channelsMenu = nuke.menu('Nodes').findItem("Channels")
#channelsMenu.addCommand('Custom Shuffle', 'nuke.createNode("Shuffle")', "alt+s", icon="Shuffle.png", shortcutContext=2)

#  ---------------------------------------------------------------
#  KEYBOARD SHORTCUTS ::::::::::::::::::::::::::::::::::::::::::::
#  ---------------------------------------------------------------

nuke.menu('Nodes').addCommand("Transform/Tracker", "nuke.createNode('Tracker4')", "ctrl+alt+t", icon="Tracker.png", shortcutContext=2)
#C:\Program Files\Nuke11.3v5\plugins\icons to find built in icons!


#  MERGE NODE SHORTCUTS ------------------------------------------
mergeMenu = nuke.menu('Nodes').findItem("Merge/Merges")
mergeMenu.addCommand('Stencil', 'nuke.createNode("Merge2", "operation stencil bbox B")', "alt+o", icon="Out.png", shortcutContext=2)
mergeMenu.addCommand('Mask', 'nuke.createNode("Merge2", "operation mask bbox A")', "alt+i", icon="In.png", shortcutContext=2)
mergeMenu.addCommand('Plus', 'nuke.createNode("Merge2", "operation plus")', "alt+]", icon="Add.png", shortcutContext=2)
mergeMenu.addCommand('From', 'nuke.createNode("Merge2", "operation from")', "alt+[", icon="From.png", shortcutContext=2)


# week 3 challenge if/else statements
#x = 15
#y = 6
#if x + y == 20:
#	print "x + y = 20! :)"
#else:
#	print "x + y = " + str(x+y) + ", not 20"

