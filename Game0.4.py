# Agenda: 
    # Move player on the screen

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

    # Here is how you can move ( Demo only)  <<<<<<<<<< ====================
    # playerX += 1
    # playerX -= 1
    # playerY += 1
    # playerY -= 1

    # Draw the player
    player(playerX,playerY)

    # update the screen
    pygame.display.update()
    
    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
