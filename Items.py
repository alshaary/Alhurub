class Weapon:
    def __init__(self):
        raise NotImplementedError("لا تنشئ أسلحة خام جديدة")
    
    def __str__(self):
        return self.name
    

class Rock(Weapon):
    def __init__(self):
        self.name = "حجر"
        self.description = "حجر بحجم اليد"
        self.damage = 5
        self.value = 1


class Dagger(Weapon):
    def __init__(self):
        self.name = "خنجر"
        self.description = "خنجر مع بعض الصداء. " \
                        "هوا أقوى من الحجر بطريقة ما."
        self.damage = 10
        self.value = 15


class RustySword(Weapon):
    def __init__(self):
        self.name = "سيف صدء"
        self.description = "هذا السيف يظهر عمره," \
                        " لكن فيه بعض الروح القتالية. "
        self.damage = 20
        self.value = 50


class Mazeltov(Weapon):
    def __init__(self):
        self.name = "مولوتوف"
        self.description = ".لألحاق ضرر بالنار"
        self.damage = 100
        self.value = 200


class Crossbow(Weapon):
    def __init__(self):
        self.name = "قوس"
        self.description = "لألحاق بعض الفجوات في الأعداء"
        self.damage = 70
        self.value = 100


# ?
class Consumable:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return "{} (+{} روح)".format(self.name, self.healing_value)


# ?
class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.healing_value = 10
        self.value = 20


class HealingPotion(Consumable):
    def __init__(self):
        self.name = "قنينة شفاء"
        self.healing_value = 50
        self.value = 60