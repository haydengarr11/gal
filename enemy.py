import os
import pygame as pg
import random

# Complete me! - TODO
class Enemy(pg.sprite.Sprite):
    def __init__(self, position):
        ships = ['Ship1.png', 'Ship2.png', 'Ship3.png'] # array of ships to add variety to the enemy ships
        whichShip = random.randint(0, 2)
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join('assets', ships[whichShip])).convert_alpha()
        imageSize = (self.image.get_rect()[2], self.image.get_rect()[3]) #gets size of image in width and height for rendering to the screen
        self.rect = pg.Rect(position, imageSize)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    # moves the enemies up or down depending on where they are 
    # positioned on the screen 
    def update(self, moveDirection):
        if (moveDirection == 0):
           self.down()
        else:
            self.up()

    def up(self):
        self.rect.y -= 1
    
    def down(self):
        self.rect.y += 1
    
    #determines if enemies are at the bottom of the screen for movement 
    def bottom(self):
        if (self.rect[1] == 735): return True
        else: return False
    
    #determines if enemies are at the top of the screen for movement 
    def top(self):
        if (self.rect[1] == 10): return True
        else: return False
    
    def getRect(self):
        return self.rect