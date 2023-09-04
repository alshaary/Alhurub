""" Text adventure game
    @year  = 2023
"""
__author__ = "alshaary"


import World
from Player import Player
from collections import OrderedDict


def play():
    print("###################")
    print("#  الهروب من الكهف  #")
    print("####################")
    World.parse_world_dsl()
    player = Player()
    while player.is_alive() and not player.victory:
        room = World.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print(" رحلتك أنتهت مبكرا ")


def get_available_actions(room, player):
    actions = OrderedDict()
    print(" :أختار حدث")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "طباعة المستودع")
    if isinstance(room, World.TraderTile):
        action_adder(actions, 't', player.trade, "متاجرة")
    if isinstance(room, World.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "هجوم")
    else:
        if World.tile_at(room.x, room.y + 1):
            action_adder(actions, 'n', player.move_north, "أذهب شمالاََ")
        if World.tile_at(room.x, room.y - 1):
            action_adder(actions, 's', player.move_south, "أذهب جنوباً")
        if World.tile_at(room.x + 1, room.y):
            action_adder(actions, 'e', player.move_east, "أذهب شرقاً")
        if World.tile_at(room.x - 1, room.y):
            action_adder(actions, 'w', player.move_west, "أذهب غرباً")
        if player.HP < 100:
            action_adder(actions, 'h', player.heal, "شفاء")
    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{} : {}".format(hotkey, name))


def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input(" :حدث")
        action = available_actions.get(action_input)
        if action:
            action()
        else:
            print("!حدث غير موجود")


play()

