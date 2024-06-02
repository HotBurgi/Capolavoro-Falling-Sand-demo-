import pygame
from const import *
import random

def spawnSand(sand):
    """
    Spawns new sand particles based on the mouse position.

    Parameters:
    - sand: 2D list representing the current state of the sand grid.
    """
    mouseX, mouseY = pygame.mouse.get_pos()
    if (0 <= mouseX < WIDTH) and (0 <= mouseY < HEIGHT):
        mCellY = mouseY // CELL
        mCellX = mouseX // CELL
        sand[mCellY][mCellX] = 1
        spawnNeighboringSand(mCellY, mCellX, sand)

# Other functions remain unchanged
