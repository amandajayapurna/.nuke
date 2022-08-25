#  ---------------------------------------------------------------------------
#   filepathLister.py
#   Version: 1.0.4
#   Last Updated: August 22, 2022
#   Author: Amanda Jayapurna
#   ! Python for Nuke Class by Ben McEwan | Class 05 + Homework Challenge
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



# assign file with scriptname to variable then open
script_name = os.path.basename(nuke.root()['name'].value())
output_file = open("C:\\Users\\ajayapurna\\Documents\\"+script_name+"_file_lister_output.txt", "w+")
# w+" argument says: "create the document if it doesn't exist, or overwrite if it does"

 #add to utilities menu
utilitiesMenu = nuke.menu('Nuke').addMenu('Utilities')
utilitiesMenu.addCommand('Filepath Lister', "filepathLister.file_lister()", "ctrl+shift+f", shortcutContext=2)


# Replace any instance of 'print' with output_file.write("string_to_write_to_file") function to write text to file.
output_file.write("Nuke Script: "+script_name)
output_file.write("\n\nFILE & VERSION LIST:\n")

# ...and also at the end of our for loop
#output_file.write("\nYou are using "+version_number+" of "+filename_no_version)
