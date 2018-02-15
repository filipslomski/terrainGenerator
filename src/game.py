import pygame

from src.init import Init
from src.Utilities.game_settings import GameSettings
from src.context import Context
from src.Utilities.colors import Colors
from src.board.board import Board
from src.events import Events


Init.initialise()

# init objects
Board.load_board_graphics()

# main game loop
while True:
    Init.clock.tick(GameSettings.FRAME_RATE)
    Init.gameDisplay.fill(Colors.BLACK)

    Events.event_control()

    # display objects
    if Context.generated_item is not None:
        Context.generated_item.display()
    Context.player.display()
    Board.display()

    pygame.display.update()
