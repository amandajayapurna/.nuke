#  ---------------------------------------------------------------------------
#   shortcut_NodeComment.py
#   Version: 1.0.0
#   Last Updated: August 24, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 06
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  - Adds ctrl + alt + c shortcut to create a node's label, so you don't waste valuable clicks opening a node and switching to the node label!!
#  ---------------------------------------------------------------------------

import nuke

def shortcut_NodeComment():
	
	selectedNode = nuke.selectedNode()
	oldComment = selectedNode['label'].value()

	inputBox = nuke.getInput("Please enter a node label", oldComment)
	selectedNode['label'].setValue(inputBox)


	if inputBox == None:
		nuke.message("Node label will remain as "+oldComment)
	else:
		selectedNode['label'].setValue(inputBox)

# add menu items
nuke.menu('Nuke').addCommand('Edit/Shortcuts/Add Comment to Node', 'shortcut_NodeComment.shortcut_NodeComment()', 'ctrl+alt+c')
