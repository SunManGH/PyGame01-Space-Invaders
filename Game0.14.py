# Agenda: Creating bullets for shooting   <<<<<<<<<< ====================

import pygame
import random

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
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

# Bullet    <<<<<<<<<< ====================
# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
alphaBulletImg = bulletImg.convert_alpha()
bulletX = 0
bulletY = 480
bulletX_change = 0  # no need to go left or right
bulletY_change = 1 # bullet is be fired up and it goes up by 1 pixels in one loop
bullet_state = "ready"

# Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

# Fire the bullet    <<<<<<<<<< ====================
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # screen.blit(alphaBulletImg, (x, y))
    screen.blit(alphaBulletImg, (x+16, y+10)) # to hide the bullet behind player

# Enemy
def enemy(x, y):
    screen.blit(enemyImg, (x, y))

# Game Loop
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    # Background Image
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
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX,bulletY)
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

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(playerX,bulletY)
        bulletY -= bulletY_change

    # Draw the player
    player(playerX, playerY)

    # Draw the enemy
    enemy(enemyX, enemyY)

    # update the screen
    pygame.display.update()


"""
Two issues observed
1- Only one bullet can be fired
2- bullet moves with player after fired
"""