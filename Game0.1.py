# Agenda: Let's close PyGame with QUIT event

import pygame

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Game Loop
running = True
while running:
 
    # https://www.pygame.org/docs/ref/event.html?highlight=pygame%20event#module-pygame.event
    # https://www.pygame.org/docs/ref/event.html?highlight=pygame%20event%20get#pygame.event.get

    # Capture and check events one by one
    for event in pygame.event.get(): #   <<<<<<<<<< ====================
        # https://www.pygame.org/docs/ref/pygame.html?highlight=quit#pygame.quit
        if event.type == pygame.QUIT:
            running = False
