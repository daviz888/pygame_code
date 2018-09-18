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
        self.img_size = self.image.get_size()
        self.rect.centerx = (ui_settings.WIDTH / 2)
        self.rect.bottom = ui_settings.HEIGHT
        self.seedx = 0

    def update(self):
        # self.rect.top -= 3
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = 5
        if keystate[pygame.K_UP]:
            self.rect.top -= 5
        if keystate[pygame.K_DOWN]:
            self.rect.top += 5
        self.rect.x += self.speedx
        if self.rect.right > self.ui_settings.WIDTH:
            self.rect.right = self.ui_settings.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= self.ui_settings.HEIGHT:
            self.rect.bottom = self.ui_settings.HEIGHT
