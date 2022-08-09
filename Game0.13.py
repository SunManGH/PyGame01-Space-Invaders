# Agenda: Better way to make it faster is calling convert() or convert_alpha()
# http://www.pygame.org/docs/ref/image.html recommends:
# For alpha transparency, like in .png images use the convert_alpha() method after loading so that the image has per pixel transparency

# Calling convert() or convert_alpha() is preferred since not doing so will mean that blits will all require pixel format conversion, which is extremely slow 
#     <<<<<<<<<< ====================

import pygame
import random

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background   <<<<<<<<<< ====================
background = pygame.image.load('background.png')
alphaImage = background.convert_alpha()

# Title (aka Caption) and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

# Enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image   <<<<<<<<<< ====================
    # screen.blit(background, (0, 0))
    screen.blit(alphaImage, (0, 0))

    # Capture and check events one by one
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Change position of the player
    playerX += playerX_change

    # Adding boundaries to our game
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:  # 800px - 64px (64px is width of pic)
        playerX = 736

    # Change position of the enemy
    enemyX += enemyX_change    

    # Enemy Movement
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:  # 800px - 64px (64px is width of pic)
        enemyX_change = -0.3
        enemyY += enemyY_change

    # Draw the player
    player(playerX, playerY)

    # Draw the enemy
    enemy(enemyX, enemyY)

    # update the screen
    pygame.display.update()
