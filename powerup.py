"""
powerups.py object
"""

import os
import sys
import random
import pygame
from pygame.sprite import Sprite

class Powerup(Sprite):
    """docstring for powerups."""
    def __init__(self, ui_settings, center):
        super().__init__()
        self.ui_settings = ui_settings
        self.power_type = random.choice(['shield', 'gun'])
        self.power_assets()
        self.image = self.power_img[self.power_type]
        self.image.set_colorkey(self.ui_settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 3

    def power_assets(self):
        self.power_img = {}
        self.power_img['shield'] = pygame.image.load(os.path.join(self.ui_settings.images_path, 'shield_gold.png')).convert()
        self.power_img['gun'] = pygame.image.load(os.path.join(self.ui_settings.images_path, 'bolt_gold.png')).convert()
        self.effects = pygame.mixer.Sound(os.path.join(self.ui_settings.sfx_path, 'sfx_shieldUp.ogg'))
        # self.effects.set_volume(0.1)

    def update(self):
        # self.rect.x += 10
        self.rect.y += self.speedy
        # kill if it moves off the top of the screenself.
        if self.rect.top > self.ui_settings.HEIGHT:
            self.kill()
