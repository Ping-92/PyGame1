import pygame

class Ship():

    def __init__(self, screen):
        """initialise ship and set starting position"""
        self.screen = screen

        # load ship image and get its rectangle
        self.image = pygame.image.load(r'C:\Users\User\PycharmProjects\PyGame1\images\ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # start each new ship at bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """draw ship at its current location"""
        self.screen.blit(self.image, self.rect)
        """screen position specified by rect"""
