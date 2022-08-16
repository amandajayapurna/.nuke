#  ---------------------------------------------------------------------------
#   shuffleShortcuts.py
#   Version: 0.1.3
#   Last Updated: August 16, 2022
#   Author: Amanda Jayapurna
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  Creates a custom shuffle node that shuffle RGBA channels into all other channels.
#  ---------------------------------------------------------------------------
import nuke
import platform
import nukescripts

def createCustomShuffle(in_channel, out_channel, set_channel, rColor, gColor, bColor):
    myShuffle = nuke.createNode('Shuffle')

    myShuffle['in'].setValue(in_channel)
    myShuffle['out'].setValue(out_channel)

    myShuffle['red'].setValue(set_channel)
    myShuffle['green'].setValue(set_channel)
    myShuffle['blue'].setValue(set_channel)
    myShuffle['alpha'].setValue(set_channel)

    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (rColor*255,gColor*255,bColor*255,1),16))
    myShuffle['label'].setValue("[value red] > [value out]")


def shuffleRGBchannels():
    #creates a variable for the selected node, before any shuffle nodes are made
    selectedNode = nuke.selectedNode()
    #variable for the x_pos and y_pos value of selected node
    selectedNode_xPos = selectedNode['xpos'].value()
    selectedNode_yPos = selectedNode['ypos'].value()

    #creates RGB shuffle nodes and assigns them to a variable after creation (last selected node)
    createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)
    redShuffle = nuke.selectedNode() 
    createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)
    greenShuffle = nuke.selectedNode()  
    createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)
    blueShuffle = nuke.selectedNode() 

    mergeShuffles = nuke.createNode('Merge2', "operation max")
    #mergeShuffles['operation'].setValue('max')    


    #sets the input of red shuffle node to selected node 
    redShuffle.setInput(0, selectedNode)
    #places the node slightly to the left/right/down in nuke port
    redShuffle['xpos'].setValue(selectedNode_xPos-150) # - left and up
    redShuffle['ypos'].setValue(selectedNode_yPos+150) # + right and down

    greenShuffle.setInput(0, selectedNode)
    greenShuffle['xpos'].setValue(selectedNode_xPos)
    greenShuffle['ypos'].setValue(selectedNode_yPos+150) 

    blueShuffle.setInput(0, selectedNode)
    blueShuffle['xpos'].setValue(selectedNode_xPos+150) 
    blueShuffle['ypos'].setValue(selectedNode_yPos+150) 

    #lesson 04 challenge 
    #extend the ShuffleRGBchannels() function to create a merge node that connects the 3 shuffle nodes, set its operation to max
    mergeShuffles.setInput(1, redShuffle)
    mergeShuffles.setInput(0, greenShuffle)
    mergeShuffles.setInput(3, blueShuffle)
    mergeShuffles['xpos'].setValue(selectedNode_xPos)
    mergeShuffles['ypos'].setValue(selectedNode_yPos+300) 
    

# Add menu.
nuke.menu('Nodes').addCommand("Channel/Shuffle (Red to ALL)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'red', 1, 0, 0)", "ctrl+shift+r", icon="redShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Green to ALL)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'green', 0, 1, 0)", "ctrl+shift+g", icon="greenShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Blue to ALL)", "shuffleShortcuts.createCustomShuffle('rgba', 'rgba', 'blue', 0, 0, 1)", "ctrl+shift+b", icon="blueShuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to ALL)", "shuffleShortcuts.createCustomShuffle('alpha', 'rgba', 'alpha', 0, 0, 1)", "ctrl+shift+a", icon="alphaToAll.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 0)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'black', 0, 0, 0)", "ctrl+shift+`", icon="alpha0Shuffle.png", shortcutContext=2)
nuke.menu('Nodes').addCommand("Channel/Shuffle (Alpha to 1)", "shuffleShortcuts.createCustomShuffle('alpha', 'alpha', 'white', 1, 1, 1)", "ctrl+shift+1", icon="alpha1Shuffle.png", shortcutContext=2)

nuke.menu('Nodes').addCommand("Channel/Shuffle (Split RGB channels)", "shuffleShortcuts.shuffleRGBchannels()", "ctrl+shift+s", icon="ShuffleSplitRGB.png", shortcutContext=2)
