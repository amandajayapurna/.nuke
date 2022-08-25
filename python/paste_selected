#  ---------------------------------------------------------------------------
#   paste_selected.py
#   Version: 1.0.2
#   Last Updated: August 22, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 05
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  - Pastes previously copied node to all selected nodes.
#  ---------------------------------------------------------------------------

import nuke

def paste_selected():

	for i in nuke.selectedNodes():
		i.setSelected(True)
		nuke.nodePaste("%clipboard%")



# Add menu.
#editMenu = nuke.menu ('Nuke').findItem("Edit")
#editMenu.addCommand("Paste Selected", 'paste_selected.paste_selected()', "ctrl+shift+v", shortcutContext=2)

nuke.menu('Nuke').addCommand('Edit/Paste to Selected', 'paste_selected.paste_selected()', 'ctrl+shift+v')

#nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to ALL)", "paste_selected.paste_selected('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)

#nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)


#channelsMenu = nuke.menu('Nodes').findItem("Channels")
#channelsMenu.addCommand('Custom Shuffle', 'nuke.createNode("Shuffle")', "alt+s", icon="Shuffle.png", shortcutContext=2)
