"""
explosion.py
"""
import sys, os
import pygame
from pygame.sprite import Sprite

class Explosion(Sprite):
	"""docstring for Explsion"""
	def __init__(self, ui_settings, sheet, width, height, center):
		super().__init__()
		self.ui_settings = ui_settings
		self.width = width
		self.height = height
		self.sheet = sheet
		# self.sheet = pygame.image.load(os.path.join(ui_settings.images_path, 'explosion.png')).convert()
		# # self.sheet = pygame.transform.scale(self.sheet, (1536, 64))
		# self.sheet.set_colorkey(self.ui_settings.BLACK)
		self.sheet_width, self.sheet_height = self.sheet.get_size()
		self.prep_sheet()
		self.image = self.animation_frame[0]
		self.rect = self.image.get_rect()
		self.rect.center = center
		self.frame = 0
		self.last_update = pygame.time.get_ticks()
		self.frame_rate = 50
		# Explosion Effects
		self.effects = pygame.mixer.Sound(os.path.join(ui_settings.sfx_path, 'rumble1.ogg'))
		self.effects.set_volume(0.1)

	def prep_sheet(self):
		self.animation_frame = []

		# Two for loops for multiple row image.
		for x in range(int(self.sheet_height / self.height)):
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
