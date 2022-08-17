#  ---------------------------------------------------------------------------
#   filepathLister.py
#   Version: 1.0.0
#   Last Updated: August 16, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 05
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  - Lists all files being read into a nuke script
#  ---------------------------------------------------------------------------

import nuke
import nukescripts
import os 
import platform


def file_lister():

	print "\n\nNuke Script: " + os.path.basename(nuke.root()['name'].value())
	print "\nFILE & VERSION LIST:"

	node_classes = ['Read', 'ReadGeo', 'Camera']
	node_list = []


	for i in nuke.allNodes():
		for x in node_classes:
			if i.knob('file') and i.Class() == x:
				node_list.append(i)

	for node in node_list:
		filepath = node['file'].value()
		filename = os.path.basename(filepath)

		filename_only = filename[0:filename.find('_v')]
		version_number = filename[filename.find('_v')+1:filename.find('_v')+6]

		print ("You are using " + version_number + " of " + filename_only)





