# Agenda: 
    # Adding images into the game
    # Create Player 

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title (aka Caption) and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png') # https://www.flaticon.com/search?word=ufo
pygame.display.set_icon(icon) 

# Player
playerImg = pygame.image.load('player.png') # https://www.flaticon.com/free-icons/space-invaders  <<<<<<<<<< ====================
# playerX = 0
# playerY = 0
# playerX = 370
# playerY = 480

def player(): #   <<<<<<<<<< ====================
    screen.blit(playerImg, (400, 400)) # blit - Wiktionary
    # screen.blit(playerImg, (playerX, playerY)) # blit - Wiktionary
    # https://en.wiktionary.org 
    # (computing) A logical operation in which a block of data is rapidly moved or copied in memory, most commonly used to animate two-dimensional graphics.

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0,0,0))

    # Draw the player #   <<<<<<<<<< ====================
    player()

    # update the screen
    pygame.display.update()
    
    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
