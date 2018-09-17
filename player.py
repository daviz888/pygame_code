"""
player.py class
"""
import pygame
from pygame.sprite import Sprite
import random

class Player(Sprite):
    """sprite for Player."""
    def __init__(self, ui_settings):
        super().__init__()
        self.ui_settings = ui_settings
        self.image = pygame.Surface((50, 50))
        self.image.fill(ui_settings.GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (ui_settings.WIDTH / 2, ui_settings.HEIGHT / 2)

    def update(self):
        self.rect.x += 5
        if self.rect.left > self.ui_settings.WIDTH:
            self.rect.right = 0
