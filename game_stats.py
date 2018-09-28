"""
game_stats.py
"""
import os
import pygame
from game_support import draw_text


class Game_Stats():
    """Game statistics for Game_Stat"""

    def __init__(self, ui_settings, screen):
        """Initializes game statistics"""
        self.ui_settings = ui_settings
        self.screen = screen
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
        self.life_percentage = 100
        self.waiting = True

    def welcome_screen(self):

        draw_text(self.screen, "SHUMP GAME", 64, self.ui_settings.WHITE, self.ui_settings.WIDTH / 2,
                  self.ui_settings.HEIGHT / 4)
        draw_text(self.screen, "User arrows to move, space to fire", 22,
                  self.ui_settings.WHITE, self.ui_settings.WIDTH / 2, self.ui_settings.HEIGHT / 2)
        draw_text(self.screen, "Press 'P' key to begin", 18, self.ui_settings.WHITE,
                  self.ui_settings.WIDTH / 2, self.ui_settings.HEIGHT * 3 / 4)
        pygame.display.flip()

        clock = pygame.time.Clock()

        while self.waiting:
            clock.tick(self.ui_settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        self.waiting = False
