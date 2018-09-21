"""
explosion.py
"""
import sys, os
import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
	"""docstring for Explsion"""
	def __init__(self, ui_settings, width, height, center):
		super().__init__()
		self.ui_settings = ui_settings
		self.width = width
		self.height = height
		self.sheet = pygame.image.load(os.path.join(ui_settings.images_path, 'explosion.png')).convert_alpha()
		self.sheet = pygame.transform.scale(self.sheet, (1536, 64))
		self.sheet_width, self.sheet_height = self.sheet.get_size()
		self.prep_sheet()

		self.image = self.animation_frame[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50

	def prep_sheet(self):
		self.animation_frame = []
		print(f'{self.width}')
		print(f'{self.sheet_width}')
		for i in range(int(self.sheet_width / self.width )):
			self.animation_frame.append(self.sheet.subsurface(( i * self.width, 0, self.width, self.height)))



	def update(self):
		now = pygame.time.get_ticks()
		if now - self.last_update > self.frame_rate:
			self.last_update = now
			self.frame += 1
			if self.frame == len(self.animation_frame):
				self.kill()
			else:
				center = self.rect.center
				self.image = self.animation_frame[self.frame]
				self.rect = self.image.get_rect()
				self.rect.center = center





