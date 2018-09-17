import sys
import pygame

class Settings():
    """game settings."""
    def __init__(self):
        # Scree constant settings.
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 30

        # Define colorsself.
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN= (0, 255, 0)

    # def loadImage(self,)
