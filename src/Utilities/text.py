import pygame
from src.init import Init


class Text:

    @classmethod
    def text_objects(cls, text, font):
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()

    @classmethod
    def message_display(cls, text, posx, posy, fontsize=20):
        largeText = pygame.font.Font('freesansbold.ttf', fontsize)
        TextSurf, TextRect = cls.text_objects(text, largeText)
        TextRect.center = (posx, posy)
        Init.gameDisplay.blit(TextSurf, TextRect)

        pygame.display.update()