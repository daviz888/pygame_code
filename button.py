'''
button.py
'''

import pygame


class Button():
    """Create a Button class object"""

    def __init__(self, ui_settings, screen, text):
        """Initialize attributes"""
        self.ui_settings = ui_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        # self.text = text

        # set the dimension and properties of the buttonself.
        self.width, self.height = 200, 50
        self.button_color = ui_settings.GREEN
        self.font = pygame.font.SysFont(ui_settings.default_font, 48)

        # build the button's rect object and center itself.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # prep the text of the buttonself.
        self.prep_text(text)

    def prep_text(self, text):
        """render text into image and center the text on the button."""
        self.text_image = self.font.render(text, True, self.ui_settings.WHITE,
                                           self.ui_settings.GREEN)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center

    def draw_button(self):
        """draw the button and the message."""
        self.screen.fill(self.ui_settings.GREEN, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
