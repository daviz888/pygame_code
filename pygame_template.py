# Pygame template - skeleton for a new pygame project

import pygame
import random

WIDTH = 360
HEIHGT = 480
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIHGT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # process inputs
    # updated
    # draw / render
    screen.fill()