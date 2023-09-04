import random
import Enemies
import Characters


class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    
    def intro_text(self):
        raise NotImplemented("قم بإنشاء فئة فرعية بدلاً من ذلك!")
    
    def modify_player(self, player):
        pass    


class StartTile(MapTile):
    def intro_text(self):
        return """
        لقد وجدت نفسك في كهف مع شعلة على الجدار
        تستطيع الخروج من أربع مخارج كلها متساوية في الظلام و الخطورة
        """


class BoringTile(MapTile):
    def intro_text(self):
        return """
        جزئية ضجرة من الكهف
        """



class VictoryTile(MapTile):
    def intro_text(self):
        return """
        أنت ترى شعاع الضوء على مسافة ...
        ... أنه يزداد كلما أقتربت, نعم أنه ضوء الشمس
        
        
        النصر لك
        """

    def modify_player(self, player):
        player.victory = True



class EnemyTile(MapTile):
    def __init__(self, x, y):
        r = random.random()
        if r < 0.50:
            self.enemy = Enemies.GiantSpider()
            self.alive_text = "عنكبوت عملاق قفز من شباكة أمامك"
            self.dead_text = "جثة عنكبوت ميت تتعفن على الأرض"
        elif r < 0.80:
            self.enemy = Enemies.Ogre()
            self.alive_text = "الغول يعيق طريقك"
            self.dead_text = "يذكرك الغول الميت بانتصارك"
        elif r < 0.95:
            self.enemy = Enemies.BatColony()
            self.alive_text = "تسمع صوت صرير يتزايد فجأة، " \
            "وتضيع وسط سرب من الخفافيش!"
            self.dead_text = "وتناثرت العشرات من الخفافيش الميتة على الأرض"
        else:
            self.enemy = Enemies.RockMonster()
            self.alive_text = "لقد أزعجت وحش الصخور من سباته!"
            self.dead_text = "بعد هزيمته، عاد الوحش إلى صخرة عادية"
        
        super().__init__(x,y)
    
    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text
        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.HP = player.HP - self.enemy.damage
            print("{} الروح المتبقية لديك .{} العدو سبب اليك ضرر"
                .format(player.HP, self.enemy.damage))

class TraderTile(MapTile):
    def intro_text(self):
        return  """ يجلس رجل ضعيف ليس بشريًا تمامًا
                    وليس مخلوقًا تمامًا في الزاوية ويربط عملاته الذهبية معًا
                    يبدو راغباً في التجارة
                """
    
    def __init__(self,x,y):
        self.trader = Characters.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} ذهب".format(i, item.name, item.value))
        while True:
            user_input = input(": للخروج 0 أختار عنصر أو أنقر على")
            if user_input == 0:
                return
            else:
                try:
                    choice = int(user_input)
                    to_swap = seller.inventory[choice - 1]
                    self.swap(seller, buyer, to_swap)
                except ValueError:
                    print("خيار غير موجود")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("هذا العنصر باهض جدا")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("المتاجرة تمت")

    def check_if_trade(self, player):
        while True:
            print("هل تود 1-الشراء 2-البيع 0-الخروج")
            user_input = input()
            if user_input == 0:
                return
            elif user_input == 1:
                print(": هذه هي العناصر المتاحة للبيع")
                self.trade(buyer = player, seller = self.trader)
            elif user_input == 2:
                print(": هذه هي العناصر المتاحة للشراء")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("خيار غير موجود")


class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.gold = player.gold + self.gold
            print("+{} قطعة ذهب مضافة".format(self.gold))

    def intro_text(self):
        if self.gold_claimed:
            return"""
                    جزء آخر غير ملحوظ من الكهف
                    يجب عليك المضي قدما
            """
        else:
            return"""
            لقد أسقط شخص ما بعض الذهب، فالتقطه
            """
        

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL غير متاح")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None


world_dsl = """
|EN|EN|VT|EN|EN|
|EN|EN|  |  |EN|
|EN|  |EN|EN|TT|
|TT|  |ST|FG|EN|
|FG|  |EN|  |FG|
"""

world_map = []

tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "  ": None}

start_tile_location = None
