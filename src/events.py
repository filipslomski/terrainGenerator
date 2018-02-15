import pygame
from src.generateItems.item_generator import ItemGenerator
from src.context import Context
from src.board.board import Board


class Events:

    @classmethod
    def event_control(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Context.generated_item = ItemGenerator.generate_item()
                if event.key == pygame.K_r:
                    Context.player.switch_item(Context.generated_item)
                #Handle graphics themes
                if event.key == pygame.K_1:
                    Board.load_board_graphics('wooden')
                if event.key == pygame.K_2:
                    Board.load_board_graphics('red')
                if event.key == pygame.K_3:
                    Board.load_board_graphics('rainbow')