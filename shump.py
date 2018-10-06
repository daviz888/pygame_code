'''
Create on October 1, 2018
about:
    shump game using pygame
By: Dovvy Pacamalan
'''
import os
import pygame
from pygame.sprite import Group
import random

from settings import Settings
from game_stats import Game_Stats
from scoreboard import Scoreboard
from player import Player
from mob import Mob
# from bullet import Bullet
from explosion import Explosion
from powerup import Powerup
from debris import Debris
import game_support as gs

# load game settings.
ui_settings = Settings()

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((ui_settings.WIDTH, ui_settings.HEIGHT))
pygame.display.set_caption("Shmup Game")
clock = pygame.time.Clock()


# Background & explosion images
background = pygame.image.load(os.path.join(ui_settings.images_path, 'universe1.png')).convert()
background = pygame.transform.scale(background, (ui_settings.WIDTH, ui_settings.HEIGHT))
background_rect = background.get_rect()

# debris = pygame.image.load(os.path.join(ui_settings.images_path, 'debris.png')).convert_alpha()
# debris_rect = debris.get_rect()

ship_explode_sheet = pygame.image.load(os.path.join(
    ui_settings.images_path, 'explosionframes.png')).convert()
ship_explode_sheet.set_colorkey(ui_settings.BLACK)

mob_explose_sheet = pygame.image.load(os.path.join(
    ui_settings.images_path, 'explosion.png')).convert_alpha()

# Spawn new mob.


def newMob():
    m = Mob(ui_settings)
    all_sprites.add(m)
    mobs.add(m)


# play background music.
ui_settings.play_music()

# Create instance of the game and statistics.
stats = Game_Stats(ui_settings, screen)
debris = Debris(ui_settings, screen)


# Game loop
game_over = True
running = True
while running:
    if game_over:
        screen.blit(background, background_rect)
        stats.welcome_screen()
        stats.reset_stats()
        game_over = False
        all_sprites = Group()
        player = Player(ui_settings)
        mobs = Group()
        bullets = Group()
        alien_bullets = Group()
        aliens = Group()
        powers = Group()
        score_board = Scoreboard(ui_settings, screen, stats, player)
        all_sprites.add(player)
        for alien in range(5):
            gs.create_aliens(ui_settings, all_sprites, aliens, alien_bullets)
            # all_sprites.add(alien)
            # all_sprites.add(alien.bullets)
            # aliens.add(alien)
        for i in range(8):
            newMob()

    # keep loop running at the right speed
    clock.tick(ui_settings.FPS)
    # Process inputs(events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()
                for bullet in player.bullets:
                    all_sprites.add(bullet)
                    bullets.add(bullet)
            elif event.key == pygame.K_ESCAPE:
                running = False

    # Updated
    all_sprites.update()
    # mobs and bullets collision.
    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        stats.score += 50 - hit.radius
        score_board.prep_score()
        explode = Explosion(ui_settings, mob_explose_sheet, 64, 64, hit.rect.center)
        explode.effects.play()
        all_sprites.add(explode)
        # Randomize the chances of getting a powerupsself.
        if random.random() > 0.9:
            power = Powerup(ui_settings, hit.rect.center)
            all_sprites.add(power)
            powers.add(power)
        m = Mob(ui_settings)
        all_sprites.add(m)
        mobs.add(m)

    # Check if the ship hit the powersself.
    powerhits = pygame.sprite.spritecollide(player, powers, True)
    if powerhits:
        for hit in powerhits:
            hit.effects.play()
            if hit.power_type == 'shield':
                player.shield += random.randrange(10, 20)
                if player.shield >= 100:
                    player.shield = 100

            elif hit.power_type == 'gun':
                player.powerup()

    # check bullets hits the alien.
    alienhits = pygame.sprite.groupcollide(aliens, bullets, True, True)
    if alienhits:
        for hits in alienhits:
            stats.score += 50 - hits.radius
            score_board.prep_score()
            explode = Explosion(ui_settings, mob_explose_sheet, 64, 64, hits.rect.center)
            explode.effects.play()
            all_sprites.add(explode)

    # check if alien bullets and shipp collide.
    ship_bullet_hits = pygame.sprite.spritecollide(player, alien_bullets, True)
    if ship_bullet_hits:
        for hits in ship_bullet_hits:
            player.shield -= 10
            if player.power > 1:
                player.power -= 1

            explode = Explosion(ui_settings, mob_explose_sheet, 64, 64, hits.rect.center)
            explode.effects.play()
            all_sprites.add(explode)

            if player.shield <= 0:
                ship_explode = Explosion(ui_settings, ship_explode_sheet, 64, 64, hits.rect.center)
                player.effects.play()
                all_sprites.add(ship_explode)
                player.hide()
                stats.lives_left -= 1
                player.shield = 100

    # check to see if mob hit the ships.
    hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
    for hit in hits:
        player.shield -= hit.radius
        if player.power > 1:
            player.power -= 1

        explode = Explosion(ui_settings, mob_explose_sheet, 64, 64, hit.rect.center)
        explode.effects.play()
        all_sprites.add(explode)
        # stats.life_percentage = player.shield
        # score_board.prep_shield_bar()
        newMob()
        if player.shield <= 0:
            ship_explode = Explosion(ui_settings, ship_explode_sheet, 64, 64, hit.rect.center)
            player.effects.play()
            all_sprites.add(ship_explode)
            player.hide()
            stats.lives_left -= 1
            player.shield = 100

    # Check if the player live is 0
    if stats.lives_left == 0 and not ship_explode.alive():
        game_over = True

    # Draw / render
    screen.fill(ui_settings.BLACK)
    screen.blit(background, background_rect)
    debris.scroll()
    # screen.blit(debris, debris_rect)
    score_board.show_scoreboard()
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
