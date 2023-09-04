import Items
import World


class Player:
    def __init__(self):
        self.inventory=[Items.Rock(),
                        Items.Dagger(),
                        Items.CrustyBread()
                        ]
        self.x = World.start_tile_location[0]
        self.y = World.start_tile_location[1]
        self.HP = 100
        self.gold = 5
        self.victory = False


    def is_alive(self):
        return self.HP > 0



    def print_inventory(self):
        print(" :المستودع")
        for item in self.inventory:
            print("-" + str(item))
        print("{} :الذهب*".format(self.gold))
        best_wepoan = self.most_powerful_weapon()
        print("{} أفضل سلاح لك هو".format(best_wepoan))
    

    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None

        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage
            except AttributeError:
                pass

        return best_weapon


    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=1)

    def move_south(self):
        self.move(dx=0, dy=-1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    
    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = World.tile_at(self.x, self.y) # ?
        enemy = room.enemy # ?
        print("{} ضد {} تستطيع أستخدام".format(enemy.name, best_weapon.name))
        enemy.HP -= best_weapon.damage
        if not enemy.is_alive():
            print("!{} لقد قتلت".format(enemy.name))
        else:
            print("{} روحه هي {}.".format(enemy.name, enemy.HP))



    def heal(self):
        consumables = [item for item in self.inventory if isinstance(item,Items.Consumable)]
        if not consumables:
            print("ليست لديك أي أغراض للشفاء")
            return

        for i, item in enumerate(consumables,1):
            print("أختار عنصر للشفاء")
            print("{}. {}".format(item,i))
        
        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice) - 2]
                self.HP = min(100, self.HP + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("{} :الروح حاليا".format(self.HP))
                valid = True
            except (ValueError, ImportError):
                print(".خيار غير متاح ,جرب مجدداً")


    def trade(self):
        room = World.tile_at(self.x, self.y)
        room.check_if_trade(self)


