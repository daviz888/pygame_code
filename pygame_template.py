# Pygame template - skeleton for a new pygame project

import pygame
import random

WIDTH = 360
HEIHGT = 480
FPS = 30

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN= (0, 255, 0)
BLUE = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIHGT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprites.Group()

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process inputs(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Updated
    all_sprites.update()
    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
