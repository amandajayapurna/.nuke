#  ---------------------------------------------------------------------------
#   shuffleShortcuts.py
#   Version: 1.0.0
#   Last Updated: August 12, 2022
#   Author: Amanda Jayapurna
#  ---------------------------------------------------------------------------

#  ---------------------------------------------------------------------------
#  USAGE:
#  Creates a shuffle node that shuffle RGBA channels into the Green channel.
#  ---------------------------------------------------------------------------

import nukescripts

def createGreenShuffle():
    myShuffle = nuke.createNode('Shuffle')
    myShuffle['red'].setValue('green')
    myShuffle['green'].setValue('green')
    myShuffle['blue'].setValue('green')
    myShuffle['alpha'].setValue('green')
    
    myShuffle['tile_color'].setValue(int('%02x%02x%02x%02x' % (0*255,1*255,0*255,1),16))
    myShuffle['label'].setValue("[value red] > [value out]")

createGreenShuffle()
