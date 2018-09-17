"""
player.py class
"""
import os
import pygame
from pygame.sprite import Sprite
import random

class Player(Sprite):
    """sprite for Player."""
    def __init__(self, ui_settings):
        super().__init__()
        self.ui_settings = ui_settings
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, 'fighter.png')).convert()
        self.image.set_colorkey(ui_settings.WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (ui_settings.WIDTH / 2, ui_settings.HEIGHT / 2)

    def update(self):
        self.rect.top -= 3
        if self.rect.bottom < 0:
            self.rect.top = self.ui_settings.HEIGHT
