import pygame

from src.init import Init
from src.Utilities.game_settings import GameSettings
Init.initialise()

# init objects

# key bindings
key_bindings = {
    pygame.K_a: 'player.move(Position(-12, 0))',
    pygame.K_d: 'player.move(Position(12, 0))',
    pygame.K_s: 'player.move(Position(0, 12))',
    pygame.K_w: 'player.move(Position(0, -12))'
}


# event control
def event_control():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key in key_bindings:
                eval(key_bindings[event.key])

# main game loop
while True:
    Init.clock.tick(GameSettings.FRAME_RATE)
    Init.gameDisplay.fill((255, 255, 255))

    event_control()

    # display objects

    pygame.display.update()