#  ---------------------------------------------------------------------------
#   shortcut_NodeCustomizer.py
#   Version: 1.0.0
#   Last Updated: August 31, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 06
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  - Adds a shortcut to change the node label, easily adds the value of a knob to the label, and set the color of the node
#  ---------------------------------------------------------------------------


import nuke

def shortcut_NodeCustomizer():

	selectedNode = nuke.selectedNode()
	oldComment = selectedNode['label'].value()
	knobList = []

	for i in selectedNode.knobs():
		knobList.append(i)

	#Create a panel
	panel = nuke.Panel("Node Customizer")

	#If the cancel button is pressed, do nothing.
	if not panel.show():
		return #aka stop processing this function and exit.
