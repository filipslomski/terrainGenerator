import pygame
import os
from src.init import Init


class Board:

    board_piece_image = None
    current_graphics = None
    board_piece_offset = {
        'wooden': 94,
        'red': 97,
        'rainbow': 97
    }

    @classmethod
    def load_board_graphics(cls, graphics='wooden'):
        cls.current_graphics = graphics
        cls.board_piece_image = pygame.image.load_extended(os.path.dirname(__file__) + "\image\\board_piece_" + graphics + ".png")

    @classmethod
    def display(cls):
        starting_height = 10
        starting_width = 250
        for i in range(0,10):
            for j in range(0, 10):
                posx = starting_width + cls.board_piece_offset[cls.current_graphics] * i
                posy = starting_height + cls.board_piece_offset[cls.current_graphics] * j
                Init.gameDisplay.blit(cls.board_piece_image, (posx, posy))