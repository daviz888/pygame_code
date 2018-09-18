"""
mob.py object
"""
import os
import pygame
from pygame.sprite import Sprite
import random

class Mob(Sprite):
    """docstring for Mod."""
    def __init__(self, ui_settings):
        super().__init__()
        self.ui_settings = ui_settings
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, 'enemy_4.png')).convert()
        # self.image = pygame.Surface((30, 40))
        # self.image.fill(self.ui_settings.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(self.ui_settings.WIDTH)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 8)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.top > self.ui_settings.HEIGHT + 10 or self.rect.left < -10 or self.rect.right > self.ui_settings.WIDTH + 10:
            self.rect.x = random.randrange(self.ui_settings.WIDTH)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
