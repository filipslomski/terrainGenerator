import random


class ItemTraits:

    defensive_pieces = ['helmet', 'armor', 'pauldrons', 'pants', 'boots', 'gauntlets']
    offensive_pieces = ['weapon']
    rarityAttributes = {
        'common' : (4, 8),
        'uncommon': (6, 12),
        'rare': (10, 20),
        'epic': (20, 40),
        'legendary': (50, 100),
    }

    @classmethod
    def get_item_traits(cls, rarity, piece):
        attack = 0
        defense = 0
        for rarity_range, attributes in cls.rarityAttributes.items():
            if random.choice(['attack', 'defense']) == 'offense':
                attack += random.randint(0, attributes[1]) if piece in cls.offensive_pieces \
                    else random.randint(0, attributes[0])
            else:
                defense += random.randint(0, attributes[1]) if piece in cls.defensive_pieces \
                    else random.randint(0, attributes[0])
            if rarity == rarity_range:
                break
        return attack, defense
