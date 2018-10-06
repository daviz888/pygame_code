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
        self.image = pygame.image.load(os.path.join(
            ui_settings.images_path, 'playerShip.png')).convert_alpha()
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
        self.shoot_delay = 250
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_time = pygame.time.get_ticks()
        self.last_shoot = pygame.time.get_ticks()

    def powerup(self):
        if self.power < 3:
            self.power += 1
            self.power_time = pygame.time.get_ticks()

    def rotate(self):
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()

    def update(self):
        # timeer for powerups.
        if self.power >= 2 and pygame.time.get_ticks() - self.power_time > self.ui_settings.POWER_UP_TIME:
            self.power = 1
            self.power_time = pygame.time.get_ticks()
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

    def shoot(self):
        # now = pygame.time.get_ticks()
        # # if now - self.last_shoot > self.shoot_delay:
        # self.last_shoot = now
        self.bullets = []
        if self.power == 1:
            self.bullets.append(Bullet(self.ui_settings, self.rect.centerx, self.rect.top, -10))
        elif self.power == 2:
            self.bullets.append(Bullet(self.ui_settings, self.rect.left, self.rect.centery, -10))
            self.bullets.append(Bullet(self.ui_settings, self.rect.right, self.rect.centery, -10))
        elif self.power == 3:
            self.bullets.append(Bullet(self.ui_settings, self.rect.centerx, self.rect.top, -10))
            self.bullets.append(Bullet(self.ui_settings, self.rect.left, self.rect.centery, -10))
            self.bullets.append(Bullet(self.ui_settings, self.rect.right, self.rect.centery, -10))
        self.bullets[0].effects.play()
