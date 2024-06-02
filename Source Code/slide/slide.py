from const import *
import random
from draw import *

def slide(futureSand, screen):
    """
    Handles the sliding of sand particles in the grid.

    Parameters:
    - futureSand: 2D list representing the future state of the sand grid.
    - screen: Pygame screen object where the sand particles will be drawn.
    """
    height = len(futureSand)
    width = len(futureSand[0])
    
    for y in range(height - 1, 0, -1):
        for x in range(width):
            if futureSand[y][x] == 1 and futureSand[y - 1][x] == 0:
                if y + 1 < height:
                    if futureSand[y + 1][x] == 1:
                        if x - 1 >= 0 and x + 1 < width:
                            if futureSand[y + 1][x - 1] == 0 and futureSand[y + 1][x + 1] == 0:
                                if random.random() < 0.5:
                                    futureSand[y][x] = 0
                                    futureSand[y + 1][x - 1] = 1
                                else:
                                    futureSand[y][x] = 0
                                    futureSand[y + 1][x + 1] = 1
                            elif futureSand[y + 1][x - 1] == 0:
                                futureSand[y][x] = 0
                                futureSand[y + 1][x - 1] = 1
                            elif futureSand[y + 1][x + 1] == 0:
                                futureSand[y][x] = 0
                                futureSand[y + 1][x + 1] = 1
                    elif x == 0:  # Left column
                        futureSand[y][x] = 0
                        futureSand[y + 1][x] = 1
                    elif x == width - 1:  # Right column
                        futureSand[y][x] = 0
                        futureSand[y + 1][x] = 1

    drawSand(futureSand, screen)
