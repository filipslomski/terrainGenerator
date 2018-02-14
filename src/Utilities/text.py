import pygame
from src.init import Init


class Text:

    @classmethod
    def text_objects(cls, text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

    @classmethod
    def message_display(cls, text, posx, posy, color, fontsize=20):
        largeText = pygame.font.Font('freesansbold.ttf', fontsize)
        TextSurf, TextRect = cls.text_objects(text, largeText, color)
        TextRect.center = (posx, posy)
        Init.gameDisplay.blit(TextSurf, TextRect)
