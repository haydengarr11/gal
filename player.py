import os
import pygame as pg

# Create a Player class that is a subclass of pygame.sprite.Sprite
# Load an image as such:
#        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
# The position is controlled by the rectangle surrounding the image.
# Set self.rect = self.image.get_rect().  Then make changes to the 
# rectangle x, y or centerx and centery to move the object.

class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'Ship6.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.y = 102
        self.numLives = 1

    #adds the player ship to the screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        pass

    # moves player up when 'w' key is pressed
    def up(self, delta):
        self.rect.y -= 5

    # moves player down when 's' key is pressed
    def down(self, delta):
        self.rect.y += 5
    
    def getRect(self):
        return self.rect