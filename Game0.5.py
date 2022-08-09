# Agenda: 
    # Keyboard input conrols and key pressed events (Part 1)
    # https://devdocs.io/pygame/ref/key

""" pygame.KEYDOWN or pygame.KEYUP
    pygame.K_UP                  up arrow
    pygame.K_DOWN                down arrow
    pygame.K_RIGHT               right arrow
    pygame.K_LEFT                left arrow
"""

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title (aka Caption) and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon) 

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480

# x and y will keep changing
def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    
    # RGB = Red, Green, Blue
    screen.fill((0,0,0))

    # Draw the player
    player(playerX,playerY)

    # update the screen
    pygame.display.update()
    
    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # pygame.key : pygame module to work with the keyboard  <<<<<<<<<< ====================
        # https://devdocs.io/pygame/ref/key
        if event.type == pygame.KEYDOWN:
            # The pygame.event queue gets pygame.KEYDOWN and pygame.KEYUP events when the keyboard buttons are pressed and released. Both events have key and mod attributes.
                # key: an integer ID representing every key on the keyboard
                # mod: a bitmask of all the modifier keys that were in a pressed state when the event occurred
            if event.key == pygame.K_LEFT:
                print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                print("Right arrow is pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Key stroke has been released")
