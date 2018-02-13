from src.generateItems.entities.item import Item
from src.generateItems.helpers.itemPiece import ItemPiece
from src.generateItems.helpers.itemRarity import ItemRarity
from src.generateItems.helpers.itemTraits import ItemTraits


class ItemGenerator:

    @staticmethod
    def generate_item():
        rarity = ItemRarity.get_item_rarity()
        piece = ItemPiece.get_piece_type()
        return Item(rarity, piece, ItemTraits.get_item_traits(rarity, piece))
