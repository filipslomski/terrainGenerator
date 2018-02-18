from src.Utilities.text import Text
from src.Utilities.colors import Colors
from src.context import Context
import random


class Points:
    attack = 0
    defense = 0

    @classmethod
    def increase_points(cls, number):
        score = random.randint(1, number)
        if random.choice(['attack', 'defense']) == 'attack':
            cls.attack += score
        else:
            cls.defense += score

    @classmethod
    def reset_points(cls):
        cls.attack = 0
        cls.defense = 0

    @classmethod
    def add_player_attributes(cls, player):
        cls.attack += player.attack
        cls.defense += player.defense

    @classmethod
    def display(cls):
        current_text_posy = 20
        text_posx = 120
        Text.message_display(
            "Attack: " + str(cls.attack) + " + " + str(Context.player.attack), text_posx, current_text_posy, Colors.RED, 35
        )
        Text.message_display(
            "Defense: " + str(cls.defense) + " + " + str(Context.player.defense), text_posx, current_text_posy + 35, Colors.BLUE, 35
        )
