import sys

import pygame


def run_game():
    # initialise game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((2560, 1440))
    pygame.display.set_caption("Ping's Alien Invasion")

    # starting main loop for the game
    while True:

        # watching for kb+m events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
