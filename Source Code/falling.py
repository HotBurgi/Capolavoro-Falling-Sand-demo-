from const import *
from draw import *
from slide import *

def futureSetup(futureSand):
    """
    Initializes the future sand grid to all zeros.

    Parameters:
    - futureSand: 2D list representing the future state of the sand grid.
    """
    height = len(futureSand)
    width = len(futureSand[0])
    for y in range(height):
        for x in range(width):
            futureSand[y][x] = 0

# Other functions remain unchanged
