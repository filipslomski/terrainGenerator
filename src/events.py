import pygame
from src.context import Context


class Events:

    @classmethod
    def event_control(cls):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    pass