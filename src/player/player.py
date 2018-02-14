from src.Utilities.game_settings import GameSettings
from src.Utilities.text import Text
from src.Utilities.colors import Colors
from src.generateItems.entities.item import Item


class Player:

    attack = 0
    defense = 0
    items = {
        "helmet": None,
        "pauldrons": None,
        "chest armor": None,
        "gauntlets": None,
        "pants": None,
        "boots": None,
        "weapon": None
    }

    def __init__(self, items = None):
        if items is not None:
            self.items = items

    def switch_item(self, item):
        self.items[item.piece] = Item(item.rarity, item.piece, item.traits)
        self.__recalculate_attributes()

    def display(self):
        current_text_posy = 50
        text_posx = GameSettings.SCREEN_WIDTH - 200
        Text.message_display("Total attack: " + str(self.attack) + "  Total defense: " + str(self.defense), text_posx, current_text_posy, Colors.YELLOW, 23)
        for piece, item in self.items.items():
            current_text_posy += 30
            if item is not None:
                Text.message_display(item.piece + " attack: " + str(item.traits['attack']) + " defense: " + str(item.traits['defense']), text_posx, current_text_posy, item.color)
            else:
                Text.message_display(piece + ": None", text_posx, current_text_posy, Colors.WHITE)

    def __recalculate_attributes(self):
        self.attack = 0
        self.defense = 0
        for piece, item in self.items.items():
            if item is not None:
                self.attack += item.traits['attack']
                self.defense += item.traits['defense']
