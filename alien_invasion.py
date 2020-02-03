import sys

import pygame


def run_game():
    # initialise game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((2560, 1440))
    pygame.display.set_caption("Ping's Alien Invasion")

    # set background colour
    bg_colour = (0,0,255)

    # starting main loop for the game
    while True:

        # watching for kb+m events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop
        screen.fill(bg_colour)

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
