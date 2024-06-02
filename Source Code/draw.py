from const import *
import pygame

def drawSand(futureSand, screen):
    """
    Draws sand particles on the screen based on the future state of the sand grid.

    Parameters:
    - futureSand: 2D list representing the future state of the sand grid.
    - screen: Pygame screen object where the sand particles will be drawn.
    """
    screen.fill((74, 74, 74))  # Fill the screen with a background color
    for y in range(ROWS):
        for x in range(COLS):
            if futureSand[x][y] == 1:
                pygame.draw.rect(screen, WHITE, (CELL * y, CELL * x, CELL, CELL))
