"""
bullet.py object
"""

import os
import sys
import random
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """docstring for Bullte."""
    def __init__(self, ui_settings, x, y, direction = 0):
        super().__init__()
        self.ui_settings = ui_settings
        # self.ship = player
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, 'shot1.png')).convert()
        self.image.set_colorkey(self.ui_settings.WHITE)
        self.rect = self.image.get_rect()
        # self.ship_rect = self.ship.rect
        self.rect.centerx = x #self.ship_rect.centerx
        self.rect.bottom = y #self.ship_rect.top
        self.direction = direction
        self.speedy = -10
        self.effects = pygame.mixer.Sound(os.path.join(ui_settings.sfx_path, 'sfx_laser2.ogg'))
        self.effects.set_volume(0.1)

    def update(self):
        self.rect.x += self.direction
        self.rect.y += self.speedy
        # kill if it moves off the top of the screenself.
        if self.rect.bottom < 0:
            self.kill()
