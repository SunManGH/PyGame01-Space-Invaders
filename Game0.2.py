# Agenda: 
    # Create icon
    # Set a title and
    # fill with background color

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title (aka Caption) and Icon #   <<<<<<<<<< ====================
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png') # https://www.flaticon.com/search?word=ufo
pygame.display.set_icon(icon) 

# Game Loop
running = True
while running:

    # completely fill the surface object with white colour
    # screen.fill(white)

    # RGB = Red, Green, Blue #   <<<<<<<<<< ====================
    # screen.fill((0, 0, 0))
    # screen.fill((255, 0, 0))
    # screen.fill((0, 255, 0))
    # screen.fill((0, 0, 255))
    screen.fill((255,255,255))

    # update the screen #   <<<<<<<<<< ====================
    pygame.display.update()
    
    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
