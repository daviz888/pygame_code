"""
debris.py object
"""
import os
import pygame
import random


class Debris():
    """docstring for Mod."""

    def __init__(self, ui_settings, screen):
        super().__init__()
        self.ui_settings = ui_settings
        self.screen = screen
        self.image = pygame.image.load(os.path.join(
            self.ui_settings.images_path, 'debris.png')).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (self.ui_settings.WIDTH, self.ui_settings.HEIGHT))
        self.rect = self.image.get_rect()
        self.rect1 = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.speedy = 1
        self.rect1.y = self.rect.height * -1
        self.rel_y = 0

    def scroll(self):
        self.rect.y += self.speedy
        self.rect1.y += self.speedy
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
        self.screen.blit(self.image, (self.rect.x, self.rect1.y))

        if self.rect.top >= self.ui_settings.HEIGHT:
            self.rect.y = self.rect.height * -1
        if self.rect1.top == self.ui_settings.HEIGHT:
            self.rect1.y = self.rect.height * -1
