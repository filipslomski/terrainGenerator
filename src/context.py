from src.player.player import Player
from src.gems.gem_logic import GemLogic


class Context:
    generated_item = None
    player = Player()
    gem_logic = GemLogic()
    player_interaction = False