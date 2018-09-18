"""
Shump Game
"""
import pygame
from pygame.sprite import Group
import random

from settings import Settings
from player import Player
from mob import Mob


# load game settings.
ui_settings = Settings()

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((ui_settings.WIDTH, ui_settings.HEIGHT))
pygame.display.set_caption("Shmup Game")
clock = pygame.time.Clock()



all_sprites = Group()
player = Player(ui_settings)
mobs = Group()
all_sprites.add(player)
for i in range(8):
    m = Mob(ui_settings)
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(ui_settings.FPS)
    # Process inputs(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Updated
    all_sprites.update()
    # Draw / render
    screen.fill(ui_settings.BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
