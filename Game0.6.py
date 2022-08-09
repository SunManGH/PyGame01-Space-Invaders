# Agenda: 
    # Keyboard input conrols and key pressed events (Part 2)
    # https://devdocs.io/pygame/ref/key

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

# To change position on X axis by some +ve or -ve number from playerX, lets create a new variable  <<<<<<<<<< ====================
playerX_change = 0

# x and y will keep changing
def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
    
    # RGB = Red, Green, Blue
    screen.fill((0,0,0))
    
    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        # Add code to change the postion   <<<<<<<<<< ====================
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Change position of the player  <<<<<<<<<< ====================
    playerX += playerX_change

    # Draw the player
    player(playerX,playerY)

    # update the screen
    pygame.display.update()