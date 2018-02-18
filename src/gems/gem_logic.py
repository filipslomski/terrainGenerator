from src.gems.board_gem import BoardGem
from src.gems.gem_types import GemTypes
import time
import random


class GemLogic:

    current_board_gems = {}

    def __init__(self):
        for i in range(0, 10):
            for j in range(0, 10):
                self.current_board_gems[(i, j)] = BoardGem(random.choice(GemTypes.get_gem_types()), (i, j))

    def generate_all_gems(self):
        for i in range(0, 10):
            for j in range(0, 10):
                self.current_board_gems[(i, j)].change_gem_type(random.choice(GemTypes.get_gem_types()))

    def display_gems(self):
        for board_position in self.current_board_gems:
                self.current_board_gems[board_position].display()

    def regenerate_if_no_moves_available(self):
        self.generate_all_gems()

    def check_if_gems_match(self):
        match_length = 0
        for i in range(0, 8):
            for j in range(0, 10):
                gem_type = self.current_board_gems[(i,j)].type
                if self.current_board_gems[(i + 1, j)] == gem_type and self.current_board_gems[(i + 2, j)].type == gem_type:
                    match_length = 3
                    if (i + 3, j) in self.current_board_gems and  self.current_board_gems[(i + 3, j)].type == gem_type:
                        match_length = 4
                        if (i + 4, j) in self.current_board_gems and self.current_board_gems[(i + 4, j)].type == gem_type:
                            match_length = 5
                    time.sleep(1)
                    self.match_gems((i, j), match_length, 'horizontal')

        for i in range(0, 10):
            for j in range(0, 8):
                gem_type = self.current_board_gems[(i,j)].type
                if self.current_board_gems[(i, j + 1)] == gem_type and self.current_board_gems[(i, j + 2)].type == gem_type:
                    match_length = 3
                    if (i, j + 3) in self.current_board_gems and  self.current_board_gems[(i, j + 3)].type == gem_type:
                        match_length = 4
                        if (i, j + 4) in self.current_board_gems and self.current_board_gems[(i, j + 4)].type == gem_type:
                            match_length = 5
                    time.sleep(1)
                    self.match_gems((i,j), match_length, 'vertical')

    def generate_gem_in_position(self, position):
        self.current_board_gems[position].change_gem_type(random.choice(GemTypes.get_gem_types()))

    def match_gems(self, position, number, axis):
        if axis == 'horizontal':
            for row_number in reversed(range(1, position[1] + 1)):
                for index in range(0, number):
                    self.current_board_gems[index, row_number].change_gem_type(self.current_board_gems[index, row_number - 1].type)
                    time.sleep(1)
            for index in range(0, number):
                self.generate_gem_in_position((index, 0))
                time.sleep(1)
        if axis == 'vertical':
            last_empty_position = position[1] + number - 1
            first_gem_to_fall_down = position[1] - 1
            while first_gem_to_fall_down >= 0:
                self.current_board_gems[position[0], last_empty_position].change_gem_type(self.current_board_gems[position[0], first_gem_to_fall_down].type)
                last_empty_position -=1
                first_gem_to_fall_down -=1
            for posy in reversed(range(0, last_empty_position + 1)):
                self.generate_gem_in_position((position[0], posy))
