#!/usr/bin/env python3

import time
import pygame as pg
import pygame.freetype
import os
from enemy import Enemy
from player import Player
from projectile import Projectile
from pygame.locals import *
import random
from eProjectile import eProjectile

def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1024, 768])
    
    # Create a player by calling the Player class to initialize
    player = Player()

    # Create enemy and projectile Groups
    enemies = pg.sprite.Group()
    projectiles = pg.sprite.Group()

    for i in range(500, 1000, 75):
        for j in range(100, 600, 50):
            enemy = Enemy((i, j))
            enemies.add(enemy)

    # Start sound - Load background music and start it
    # playing on a loop - TODO
    # referenced http://www.pygame.org/docs/ref/music.html on how to load and play 
    # on
    pg.mixer.music.load("./assets/cpu-talk.mp3")
    pg.mixer.music.play(loops = -1)
    #background gets the image from assets that is the background for the game
    background = pg.image.load("./assets/UbuxB7.png")

    # Get font setup
    pg.freetype.init()
    font_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "./assets", "PermanentMarker-Regular.ttf")
    font_size = 64
    font = pg.freetype.Font(font_path, font_size)
    FONT_COLOR = (243, 45, 159)
    # Startup the main game loop
    running = True
    # Keep track of time
    delta = 0
    # Make sure we can't fire more than once every 250ms
    shotDelta = 250
    # Make sure the enemies can't fire more than once every 500ms
    enemyShotDelta = 500
    # ship movement variable that is 1 for up and 0 for down
    # used in the movement loop while running
    enemyMovement = 0
    # Frame limiting
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    # Setup score variable
    score = 0
    # The number of player lives
    while running:

        if (score < 7000):
            # First thing we need to clear the events.
            # event +1 is the player shooting the enemy 
            # and +2 is the enemy firing at the player
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.USEREVENT + 1:
                    score += 100
                if event.type == pg.USEREVENT + 2:
                    running = False
            keys = pg.key.get_pressed()

            if keys[K_s]:
                if (player.rect[1] < 695):
                    player.down(delta)
            if keys[K_w]:
                if (player.rect[1] > 102):
                    player.up(delta)

            
            for enemy in enemies:
                if (enemy.bottom()):
                    enemyMovement = 1 # Move enemy ships up
                if (enemy.top()):
                    enemyMovement = 0 # Move enemy ships down
            


            # shooting for the player and the enemy
            # if the player presses the spacebar and the time is after 250ms 
            # from the previous shot
            if keys[K_SPACE]:
                if shotDelta >= .25:
                    projectile = Projectile(player.rect, enemies)
                    projectiles.add(projectile)
                    shotDelta = 0
            
            # the enemy shot is at random and the ship that shoots the 
            # shot is a random enemy
            if enemyShotDelta >= 1:
                enemyShotDelta = 0
                shootAtPlayer = random.randint(0, 1)
                if (shootAtPlayer == 1):
                    enemyShotShip = enemies.sprites()[random.randint(0, len(enemies) - 1)]
                    enemyProjectile = eProjectile(enemyShotShip.getRect(), player)
                    projectiles.add(enemyProjectile)

            # Ok, events are handled, let's update objects!
            # Updating all enemies, the player, and the projectile
            player.update(delta)
            for enemy in enemies:
                enemy.update(enemyMovement)
            for projectile in projectiles:
                projectile.update(delta)

            # Objects are updated, now let's draw!
            screen.fill((0, 0, 0))
            #added in a screen background 
            screen.blit(background, (10,10)) 
            player.draw(screen)
            enemies.draw(screen)
            projectiles.draw(screen)


            # if all enemies are defeated then the player will have 7000 pts and
            # they win. Otherwise, it will show the score in the upper left hand corner along with
            # the amount of time it has taken in seconds
            if (score == 7000):
                font.render_to(screen, (320, 320), "You Win!", FONT_COLOR, None, size=64)
                font.render_to(screen, (320, 380), "Score: 7000", FONT_COLOR, None, size=64)
            else:
                font.render_to(screen, (10, 10), "Score: " + str(score), FONT_COLOR, None, size=64)
                font.render_to(screen, (10, 75), "Time: " + str((pg.time.get_ticks() / 1000)), FONT_COLOR, None, size=16)


            # When drawing is done, flip the buffer.
            pg.display.flip()

            # How much time has passed this loop?
            delta = clock.tick(fps) / 1000.0
            shotDelta += delta
            enemyShotDelta += delta
        else:
            running = False

# Startup the main method to get things going.
if __name__ == "__main__":
    main()
    pg.quit()