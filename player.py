"""
player.py class
"""
import os
import pygame
from pygame.sprite import Sprite
import random
from bullet import Bullet

class Player(Sprite):
    """sprite for Player."""
    def __init__(self, ui_settings):
        super().__init__()
        self.ui_settings = ui_settings
        self.image = pygame.image.load(os.path.join(ui_settings.images_path, 'playerShip.png')).convert_alpha()
        self.effects = pygame.mixer.Sound(os.path.join(ui_settings.sfx_path, 'expl1.ogg'))
        self.image.set_colorkey(ui_settings.WHITE)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .80 / 2)
        # pygame.draw.circle(self.image, ui_settings.RED, self.rect.center, self.radius)
        self.img_size = self.image.get_size()
        self.rect.centerx = (ui_settings.WIDTH / 2)
        self.rect.bottom = ui_settings.HEIGHT
        self.seedx = 0
        self.shield = 100
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()

    def rotate(self):
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.tim

    def update(self):
        # self.rect.top -= 3
        # undide ship if hiddenself.
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = (self.ui_settings.WIDTH / 2)
            self.rect.bottom = self.ui_settings.HEIGHT
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

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (self.ui_settings.WIDTH / 2, self.ui_settings.HEIGHT + 200)
