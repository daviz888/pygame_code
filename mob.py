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
        self.file_name = str(random.randrange(0,6)) + '.png'
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, self.file_name)).convert_alpha()
        self.image = pygame.transform.scale(self.image,(40, 40))
        # self.image.set_colorkey(ui_settings.BLACK)
        self.effects = pygame.mixer.Sound(os.path.join(ui_settings.sfx_path, 'expl1.ogg'))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 / 2)
        # pygame.draw.circle(self.image, self.ui_settings.GREEN, self.rect.center, self.radius  )
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

