import pygame

from src.init import Init
from src.Utilities.game_settings import GameSettings
from src.context import Context
from src.Utilities.colors import Colors
from src.events import Events


Init.initialise()

# init objects

# main game loop
while True:
    Init.clock.tick(GameSettings.FRAME_RATE)
    Init.gameDisplay.fill(Colors.BLACK)

    Events.event_control()

    # display objects


    pygame.display.update()

