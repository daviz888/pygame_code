import os
import sys
import pygame


def draw_text(screen, text, size, color, x, y):
    default_font = pygame.font.match_font('arial')
    font = pygame.font.SysFont(default_font, size)
    text_surface = font.render(text, True, color, None)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)
