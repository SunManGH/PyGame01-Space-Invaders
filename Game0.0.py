# Agenda: Create PyGame with minimum code and Intro to PyGame

# https://www.pygame.org/docs
# https://devdocs.io/pygame/

''' Minimum code you need to create any PyGame program '''
import pygame

# Intialize the pygame
# https://www.pygame.org/docs/tut/ImportInit.html
pygame.init()

# create the screen with method set_mode(size: _Coordinate = (0, 0))
# https://www.pygame.org/docs/ref/display.html#module-pygame.display
# https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

pygame.display.set_mode(size=(800, 600)) # (width, height) (x,y) and Top left is (0,0)

# Game Loop

# To Keep the screen up and running, let's create a hack
while True:
    pass
