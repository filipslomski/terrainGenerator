from src.Utilities.text import Text
from src.Utilities.game_settings import GameSettings
from src.Utilities.colors import Colors


class Item:

    rarity = None
    piece = None
    color = None

    rarity_color = {
        'legendary': Colors.BRONZE,
        'epic': Colors.VIOLET,
        'rare': Colors.BLUE,
        'uncommon': Colors.GREEN,
        'common': Colors.WHITE
    }

    traits = {
        'attack': 0,
        'defense': 0
    }

    def __init__(self, rarity, piece, traits):
        self.rarity = rarity
        self.color = self.rarity_color[self.rarity]
        self.piece = piece
        self.traits = traits

    def display(self):
        Text.message_display(
            self.piece + " attack: " + str(self.traits['attack']) + " defense: " + str(self.traits['defense'])
            ,GameSettings.SCREEN_WIDTH / 2,
            GameSettings.SCREEN_HEIGHT / 2,
            self.color
        )

