# Agenda: Adding text and display score
#   <<<<<<<<<< ====================

import math

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

# Bullet
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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)


# Score   <<<<<<<<<< ====================
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

# Where to display the score?  <<<<<<<<<< ====================
textX = 10
testY = 10


# Show score   <<<<<<<<<< ====================
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def player(x, y):
    screen.blit(playerImg, (x, y))

# Fire the bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    # screen.blit(alphaBulletImg, (x, y))
    screen.blit(alphaBulletImg, (x+16, y+10)) # to hide the bullet behind player

# Enemy
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

# Collision detection
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

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
                playerX_change = -1     #   <<<<<<<<<< ====================
            if event.key == pygame.K_RIGHT:
                playerX_change = 1     #   <<<<<<<<<< ====================
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
                    
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

    # Enemy Movement
    for i in range(num_of_enemies):
        # Change position of the enemy
        enemyX[i] += enemyX_change[i]

        # Enemy Movement
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50, 150)

        # Draw the enemy
        enemy(enemyX[i], enemyY[i], i)

    # Change bullet state to Y 480 again if goes beyond 0
    if bulletY < 0:
        bulletY = 480
        bullet_state = "ready"

    # Bullet Movement
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # Draw the player
    player(playerX, playerY)

    # Show the score     #   <<<<<<<<<< ====================
    show_score(textX, testY)

    # update the screen
    pygame.display.update()
