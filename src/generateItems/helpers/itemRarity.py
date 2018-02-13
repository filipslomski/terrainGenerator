import random


class ItemRarity:

    rarities = {
        5: 'legendary',
        15: 'epic',
        30: 'rare',
        55: 'uncommon',
        100: 'common'
    }

    @classmethod
    def get_item_rarity(cls):
        random_seed = random.randint(1, 100)
        for drop_chance, rarity in cls.rarities.items():
            if random_seed <= drop_chance:
                return rarity