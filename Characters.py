import Items


class NonPlayableCharacter():
    def __init__(self):
        raise NotImplementedError(".لا تنشئ مواد خام للشخصية الغير قابلة للعب")
    

    def __str__(self):
        return self.name

class Trader(NonPlayableCharacter):
    def __init__(self):
        self.name = "التاجر"
        self.gold = 100
        self.inventory = [Items.CrustyBread(),
                        Items.CrustyBread(),
                        Items.CrustyBread(),
                        Items.HealingPotion(),
                        Items.HealingPotion()]
