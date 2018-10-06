import os
import sys
import pygame
from alien import Alien


def draw_text(screen, text, size, color, x, y):
    default_font = pygame.font.match_font('arial')
    font = pygame.font.SysFont(default_font, size)
    text_surface = font.render(text, True, color, None)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def create_aliens(ui_settings, all_sprites, aliens, alien_bullets):
    for n in range(5):
        alien = Alien(ui_settings, all_sprites, alien_bullets)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * n
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height
        all_sprites.add(alien)
        aliens.add(alien)
