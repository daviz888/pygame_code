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
    def __init__(self, ui_settings, x, y):
        super().__init__()
        self.ui_settings = ui_settings
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, 'shot.png'))
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screenself.
        if self.rect.bottom < 0:
            self.kill()
