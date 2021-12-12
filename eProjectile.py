import os
import pygame as pg


# used the given projectile.py to outline the enemies projectile
# instead an enemy is used that is shooting the shot 
class eProjectile(pg.sprite.Sprite):
    def __init__(self, shipLocation, enemy):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('assets', 'shot.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = shipLocation.x + 30
        self.rect.centery = shipLocation.y + 15
        self.enemy = enemy
        self.event = pg.USEREVENT + 2
        self.fireSound = pg.mixer.Sound("./assets/fire.wav")
        self.fireSound.play()
        self.explosionSound = pg.mixer.Sound("./assets/explosion.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.x -= 1000 * delta
        if self.rect.x < 0:
            self.kill()
        collision = pg.sprite.collide_rect(self, self.enemy)
        if collision:
            self.enemy.kill()
            pg.event.post(pg.event.Event(self.event))
            self.explosionSound.play()
            self.kill()