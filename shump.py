"""
Shump Game
"""
import os
import pygame
from pygame.sprite import Group
import random

from settings import Settings
from game_stats import Game_Stats
from scoreboard import Scoreboard
from player import Player
from mob import Mob
from bullet import Bullet
from explosion import Explosion

# load game settings.
ui_settings = Settings()

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((ui_settings.WIDTH, ui_settings.HEIGHT))
pygame.display.set_caption("Shmup Game")
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join(ui_settings.images_path, 'space.png')).convert()
background = pygame.transform.scale(background, (ui_settings.WIDTH, ui_settings.HEIGHT))
background_rect = background.get_rect()

# play background music.
ui_settings.play_music()

# Create instance of the game and statistics.
stats = Game_Stats(ui_settings)
score_board = Scoreboard(ui_settings, screen, stats)

all_sprites = Group()
player = Player(ui_settings)
mobs = Group()
bullets = Group()
all_sprites.add(player)
for i in range(8):
    m = Mob(ui_settings)
    all_sprites.add(m)
    mobs.add(m)

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(ui_settings.FPS)
    # Process inputs(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(ui_settings, player)
                bullet.effects.play()
                all_sprites.add(bullet)
                bullets.add(bullet)
    # Updated
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        stats.score += 50 - hit.radius
        score_board.prep_score()
        m.effects.play()
        explode = Explosion(ui_settings, 64, 64, hit.rect.center) 
        all_sprites.add(explode)
        m = Mob(ui_settings)
        all_sprites.add(m)
        mobs.add(m)

    # check to see if mob hit the ships.
    hits = pygame.sprite.spritecollide(player, mobs, False, pygame.sprite.collide_circle)

    if hits:
        player.effects.play()
        running = False

    # Draw / render
    screen.fill(ui_settings.BLACK)
    screen.blit(background, background_rect)
    all_sprites.draw(screen)
    score_board.show_score()
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
