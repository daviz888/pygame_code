import os
import pygame
from pygame.sprite import Sprite
import random


class Settings():
    """game settings."""

    def __init__(self):
        # Scree constant settings.
        # pygame.init()
        pygame.mixer.init()
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 50
        self.POWER_UP_TIME = 5000  # milliseconds

        # Define colorsself.
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)

        # setup asset folders
        self.game_path = os.path.dirname(__file__)
        self.images_path = os.path.join(self.game_path, 'images')
        self.sfx_path = os.path.join(self.game_path, 'sounds')

        # set default fonts
        self.default_font = pygame.font.match_font('arial')

        # Players lives limit
        self.lives_limit = 1

        # Set sound effects
        self.backgroundMusic = pygame.mixer.music.load(os.path.join(self.sfx_path, 'intro.ogg'))
        # self.backgroundMusic.set_volume(0.1)
        pygame.mixer.music.set_volume(0.1)

        # Define life Bars.
        self.LIFE_BAR_LENGTH = 100
        self.LIFE_BAR_HEIGHT = 10

    def play_music(self):
        pygame.mixer.music.play(-1)
