#  ---------------------------------------------------------------------------
#   listNavigator.py
#   Version: 1.0.0
#   Last Updated: August 16, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 05
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  - Lists selected nodes alphabetically
#  - Show details about the list in a message box.
#  ---------------------------------------------------------------------------

import nuke

def listNavigator():

	node_list = []

	for i in nuke.selectedNodes():
		node_list.append(i.name())

		node_list.sort()

	print "NODES IN LIST:\n"

	for i in node_list:
		print "- " + i

	nuke.message("There are "+str(len(node_list))+" nodes in this list.\n\nThe first node in the list is "+node_list[0]+".\nThe last node in the list is "+node_list[-1]+"\n\nSee the script editor for all nodes in list, sorted alphabetically...")


