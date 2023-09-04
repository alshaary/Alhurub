class Enemy:
    def __init__(self):
        raise NotImplementedError("لا تنشئ كائنات عدو خام")


    def __str__(self):
        return self.name

    def is_alive(self):
        return self.HP > 0


class GiantSpider(Enemy):
    def __init__(self):
        self.name = "عنكبوت عملاق"
        self.HP = 10
        self.damage = 2

class Ogre(Enemy):
    def __init__(self):
        self.name = "غول"
        self.hp = 30
        self.damage = 10


class BatColony(Enemy):
    def __init__(self):
        self.name = "مستعمرة الخفافيش"
        self.hp = 100
        self.damage = 4


class RockMonster(Enemy):
    def __init__(self):
        self.name = "وحش صخري"
        self.hp = 80
        self.damage = 15

