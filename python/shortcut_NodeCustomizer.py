#  ---------------------------------------------------------------------------
#   shortcut_NodeCustomizer.py
#   Version: 1.0.1
#   Last Updated: September 11th, 2022
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

	#sort list alphabetically
	knobList.sort()
	knobList.insert(0,'None')

	knobList_string = " ".join(knobList)

	#Create a panel
	panel = nuke.Panel("Node Customizer")

	#add UI knobs
	panel.addSingleLineInput("Comment", oldComment)
	panel.addEnumerationPulldown("Knob", knobList_string)
	panel.addBooleanCheckBox("Change Node Colour?", False) #false means unchecked, true means checked

	#If the cancel button is pressed, do nothing.
	if not panel.show():
		return #aka stop processing this function and exit.

	#Attach values of panel's knobs to variables to use later
	comment_input = panel.value("Comment") 
	knob_choice = panel.value("Knob")
	node_label = comment_input + "\n" + knob_choice +": [value "+knob_choice+"]"


	#Making sure there are no bugs!
	#Change values on our selected node from user choice

	#if user does not enter data or make changes, pop open a message and exit the window
	if comment_input == "" and panel.value("Knob") == "None" and panel.value("Change Node Colour?") == False:
		nuke.message("Please enter a node label")
		return

	#if a label is typed but no knob value selected, set the selected node's label to the comment_input
	elif knob_choice == "None":
		selectedNode['label'].setValue(comment_input)

	#if no label is typed but a knob value is selected, set the selected node's label to display the knob's value
	elif comment_input == "":
		selectedNode['label'].setValue(knob_choice+": [value "+knob_choice+"]")

	#If none of these conditions are met, set the selected node's label to display both comment_input and knob_choice (the node_label variable)
	else:
		selectedNode['label'].setValue(node_label)

	#Check if the checkbox to change color is checked. if yes, pop open color picker window
	if panel.value("Change Node Colour?") == True:
		selectedNode['tile_color'].setValue(nuke.getColor())
	else:
		return

#Add Menu Items-- nicer, more modular way to work
nuke.menu('Nuke').addCommand('Utilities/Node Customizer', 'shortcut_NodeCustomizer.shortcut_NodeCustomizer()', 'ctrl+alt+c')



	
