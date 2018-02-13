from src.Utilities.text import Text
from src.Utilities.game_settings import GameSettings


class Item:

    rarity = None
    piece = None
    traits = None

    def __init__(self, rarity, piece, traits):
        self.rarity = rarity
        self.piece = piece
        self.traits = traits

    def display(self):
        Text.message_display(
            "Rarity: " + self.rarity + " Piece: " + self.piece + " Attributes: " + str(self.traits[0]) + " " + str(self.traits[1])
            ,GameSettings.SCREEN_WIDTH / 2,
            GameSettings.SCREEN_HEIGHT / 2
        )

