import pygame
import os
from src.init import Init
from src.Utilities.game_settings import GameSettings


class BoardGem:

    path_to_image = None
    image = None
    type = None
    board_position = None # tuple

    def __init__(self, type, board_position):
        self.type = type
        self.__set_image_path(self.type)
        self.board_position = board_position

    def display(self):
        board_piece_offset = 95
        gems_starting_width = GameSettings.BOARD_WIDTH + 20
        gems_starting_height = GameSettings.BOARD_HEIGHT + 20
        posx = gems_starting_width + board_piece_offset * self.board_position[0]
        posy = gems_starting_height + board_piece_offset * self.board_position[1]
        Init.gameDisplay.blit(self.image, (posx, posy))

    def change_gem_type(self, new_type):
        self.type = new_type
        self.__set_image_path(self.type)

    def __set_image_path(self, gem_type):
        self.image = pygame.image.load_extended(
            os.path.dirname(__file__) + "\images\\"+ gem_type +"_gem.png")