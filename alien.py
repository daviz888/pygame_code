"""
alien.py object
"""
import os
import pygame
from pygame.sprite import Sprite
from bullet import Bullet
import random


class Alien(Sprite):
    """docstring for Alien."""

    def __init__(self, ui_settings, all_sprites, alien_bullets):
        super().__init__()
        self.ui_settings = ui_settings
        self.all_sprites = all_sprites
        self.alien_bullets = alien_bullets
        self.file_name = str(random.randrange(5, 9)) + '.png'
        self.image = pygame.image.load(os.path.join(
            ui_settings.images_path, self.file_name)).convert_alpha()
        # self.image = pygame.transform.scale(self.image,(40, 40))
        # self.image.set_colorkey(ui_settings.BLACK)
        # self.effects = pygame.mixer.Sound(os.path.join(ui_settings.sfx_path, 'expl1.ogg'))
        # self.effects.set_volume(0.1)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .8 / 2)
        # pygame.draw.circle(self.image, self.ui_settings.GREEN, self.rect.center, self.radius  )
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.speedy = 1
        self.speedx = 1
        self.power = 1
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 1000

    def update(self):
        # self.rect.y += self.speedy
        self.rect.x += self.speedx
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.shoot()
        # self.rect.x += self.speedx
        # if self.rect.top > self.ui_settings.HEIGHT + 10 or self.rect.left < -10 or self.rect.right > self.ui_settings.WIDTH + 10:
        #     for n in range(5):
        #         self.rect.x = self.rect.width
        #         self.rect.y = self.rect.height
        #         self.speedy = 1
        if self.rect.right >= self.ui_settings.WIDTH:
            self.speedx = -1
            self.rect.y += 1
        elif self.rect.left <= 0:
            self.speedx = 1
            self.rect.y += 1

    def shoot(self):
        # self.bullets = []
        bullet = Bullet(self.ui_settings, self.rect.centerx, self.rect.bottom, 10)
        bullet.effects.play()
        self.all_sprites.add(bullet)
        self.alien_bullets.add(bullet)

    # def check_edge(self):
    #     if self.rect.right >= self.ui_settings.WIDTH:
    #         self.speedx = -1
    #     elif self.rect.left <= 0:
    #         self.speedx = 1
