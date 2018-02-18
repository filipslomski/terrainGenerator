import pygame

from src.init import Init
from src.Utilities.game_settings import GameSettings
from src.context import Context
from src.Utilities.colors import Colors
from src.board.board import Board
from src.events import Events
from src.points import Points


Init.initialise()

# init objects
Board.load_board_graphics()
check_for_match = True

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
    Context.gem_logic.display_gems()
    Points.display(Context.player)

    pygame.display.update()

    if check_for_match or Context.player_interaction:
        check_for_match = Context.gem_logic.check_if_gems_match()
        Context.player_interaction = False
