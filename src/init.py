import pygame

from src.Utilities.game_settings import GameSettings


class Init:

    gameDisplay = None
    clock = None
    display_width = GameSettings.SCREEN_WIDTH
    display_height = GameSettings.SCREEN_HEIGHT
    caption = GameSettings.SCREEN_CAPTION

    @classmethod
    def initialise(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption(self.caption)
        self.clock = pygame.time.Clock()