import sys

import pygame

from settings import Settings


def run_game():
    # initialise game, settings and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    pygame.display.set_caption("Ping's Alien Invasion")

    # set background colour
    bg_colour = (0, 0, 255)

    # starting main loop for the game
    while True:

        # watching for kb+m events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # redraw the screen during each pass through the loop
        screen.fill(ai_settings.bg_colour)

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
