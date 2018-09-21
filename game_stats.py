"""
game_stats.py
"""
class Game_Stats():
	"""Game statistics for Game_Stat"""
	def __init__(self, ui_settings):
		"""Initializes game statistics"""
		self.ui_settings = ui_settings
		self.reset_stats()

		# Start the game in the active state.
		self.game_active = False

		# High score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can be change during the game."""
		self.lives_left = self.ui_settings.lives_limit
		self.score = 0
		self.level = 1