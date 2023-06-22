import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleert"""
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #Load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        #start each alien at top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store exact horizontal position of the alien
        self.x = float(self.rect.x)