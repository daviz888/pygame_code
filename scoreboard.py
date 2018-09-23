"""
scoreboard.py
"""
import os, sys
import pygame

class Scoreboard():
	"""docstring for Scoreboard"""
	def __init__(self, ui_settings, screen, stats):
		self.ui_settings = ui_settings
		self.screen = screen
		self.screen_rect = self.screen.get_rect()
		self.stats = stats

		# Font settings for scoring information
		# self.text_color = self.ui_settings.WHITE
		self.font = pygame.font.SysFont(self.ui_settings.default_font, 48)

		# Prepare the initial image.
		self.prep_score()
		self.prep_shield_bar()


	def prep_score(self):
		""" Turn the score into rendered image."""
		str_score = "{:,}".format(int(round(self.stats.score, -1)))
		self.score_image = self.font.render(str_score, True, self.ui_settings.WHITE, None)	

		# Display the score at the right top of the screen.
		self.score_rect = self.score_image.get_rect()
		self.score_rect.right = self.screen_rect.right - 20
		self.score_rect.top = 20

	def prep_shield_bar(self):
		"""Life bar indicator"""
		if self.stats.life_percentage < 0:
			self.stats.life_percentage = 0
		self.fill = (self.stats.life_percentage / 100) * self.ui_settings.LIFE_BAR_LENGTH
		self.outline_rect = pygame.Rect(5, 5, self.ui_settings.LIFE_BAR_LENGTH, self.ui_settings.LIFE_BAR_HEIGHT)
		self.fill_rect = pygame.Rect(5, 5, self.fill, self.ui_settings.LIFE_BAR_HEIGHT)

	def show_scoreboard(self):
		""" Draw the score to the screen."""
		self.screen.blit(self.score_image, self.score_rect)
		pygame.draw.rect(self.screen, self.ui_settings.GREEN, self.fill_rect)
		pygame.draw.rect(self.screen, self.ui_settings.WHITE, self.outline_rect, 2)
		


		
