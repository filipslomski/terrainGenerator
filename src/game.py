import pygame

from src.init import Init
from src.Utilities.game_settings import GameSettings
from src.generateItems.item_generator import ItemGenerator
from src.Utilities.colors import Colors
from src.player.player import Player


Init.initialise()

# init objects
generated_item = None
player = Player()

# event control
def event_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                global generated_item
                generated_item = ItemGenerator.generate_item()
            if event.key == pygame.K_r:
                player.switch_item(generated_item)

# main game loop
while True:
    Init.clock.tick(GameSettings.FRAME_RATE)
    Init.gameDisplay.fill(Colors.BLACK)

    event_control()

    # display objects
    if generated_item is not None:
        generated_item.display()
    player.display()

    pygame.display.update()