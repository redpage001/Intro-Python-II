from room import Room
from player import Player
from item import Item
from monster import Monster

# Declare all the rooms

room = {
    'outside cave entrance':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'grand overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in the distance, but there is no 
way across the chasm."""),

    'narrow passage':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers. You do find 
a door that leads to the north, however, but it appears to be locked."""),

    'secret passage': Room("Secret Passage", """The secret passage heads north and forks both
east and west. You feel a breeze coming fro the west and you hear something breathing faintly
to the east."""),

    'deep valley': Room("Deep Valley", """You exit the passage into a deep valley. The steep cliffs
that wall up the valley are to trecherous to climb. Your only course of action is to turn back."""),

    'forked passage': Room("Forked Passage", """The passage leads east where you see a fork to the
south. You hear deep breathing accompanied by a wave of heat eminating from the south passage. Coming
from the east you hear what sounds like bones clattering."""),

    'dragon burrow': Room("Dragon Burrow", """You enter the a large cavern where you see a giant 
dragon prowling around the room! Beyond the dragon you see a passage to the east lit by a golden light."""),

    'skeleton arena': Room("Skeleton Arena", """The passage leads to a large room where an armored
skeleton awaits you, sword in hand! It blocks the path to the south where you see golden light."""),

    'real treasure room': Room("Real Treasure Room", """Congratulations! You found the true lost treasure! 
Piles upon piles of gold fill the room along with other treasures! You're now richer than you can ever hope 
to be!""")

}

# Declare all the items

item_list = {
    'sword': Item("Sword", "You've found a steel sword on the ground. It could be handly along the way."),
    'shield': Item("Shield", "You found an iron shield lying against the wall. It looks well worn but sturdy."),
    'key': Item("Key", "You found an old key. It looks to be very important."),
    'lantern': Item("Lantern", "You find a golden lantern which emits a bright light throughout the area.")
}

# Declare all Monsters

monster_list = {
    'dragon': Monster("Dragon", "The dragon rears up and breathes a plume of white hot fire upon you, without a sword and shield you are powerless as you are burnt to a crisp.", "The dragon rears up and breathes a plume of white hot fire upon you. Thinking quickly you bring up your shield to protect against the fire and you slay the dragon with your sword."),
    'skeleton knight': Monster("Skeleton Knight", "The skeleton knight rushes at you and without a sword and shield yourself, it skewers you with its sword.", "With your sword you easily dispatch the skeleton knight, sending it clattering to the ground in pieces.")
}

# Link rooms together

room['outside cave entrance'].n_to = room['foyer']
room['foyer'].s_to = room['outside cave entrance']
room['foyer'].n_to = room['grand overlook']
room['foyer'].e_to = room['narrow passage']
room['grand overlook'].s_to = room['foyer']
room['narrow passage'].w_to = room['foyer']
room['narrow passage'].n_to = room['treasure chamber']
room['treasure chamber'].s_to = room['narrow passage']
room['treasure chamber'].n_to = room['secret passage']
room['secret passage'].s_to = room['treasure chamber']
room['secret passage'].w_to = room['deep valley']
room['secret passage'].e_to = room['forked passage']
room['deep valley'].e_to = room['secret passage']
room['forked passage'].w_to = room['secret passage']
room['forked passage'].e_to = room['skeleton arena']
room['forked passage'].s_to = room['dragon burrow']
room['skeleton arena'].w_to = room['forked passage']
room['skeleton arena'].s_to = room['real treasure room']
room['dragon burrow'].n_to = room['forked passage']
room['dragon burrow'].e_to = room['real treasure room']
room['real treasure room'].n_to = room['skeleton arena']
room['real treasure room'].w_to = room['dragon burrow']

#Which rooms are dark

room['foyer'].is_lit = False
room['narrow passage'].is_lit = False
room['secret passage'].is_lit = False

#Which rooms are locked

room['secret passage'].is_locked = True

item_list['lantern'].light = True

#Fill rooms with items

room['foyer'].add_item(item_list['sword'])
room['grand overlook'].add_item(item_list['key'])
room['treasure chamber'].add_item(item_list['lantern'])
room['deep valley'].add_item(item_list['shield'])

#FIll rooms with monsters

room['dragon burrow'].add_monster(monster_list['dragon'])
room['skeleton arena'].add_monster(monster_list['skeleton knight'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input(" \n Enter Player Name here: \n ")
player = Player(player_name, room['outside cave entrance'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

running = True

while running:
    print(f"========== {player.current_room.name} ==========")
    player_input = input(' \n Use "w" key to move North, "a" key to move West, "d" key to move East, "s" key to move South, "i" key to open inventory, "o" key to search the room, and "q" key to quit game: \n ')
    notNorth = " \n There is no path to the North.\n "
    notWest = " \n There is no path to the West.\n "
    notEast = " \n There is no path to the East.\n "
    notSouth = " \n There is no path to the South.\n "

    if player_input == "w":
        if player.current_room.n_to != None and (not player.current_room.n_to.is_locked or player.inventory.__contains__(item_list['key'])):
            if player.inventory.__contains__(item_list['key']) and player.current_room.n_to.is_locked:
                print(" \n You used the key to open the locked door. \n ")
                player.current_room = player.current_room.n_to
                print(f" \n {player.current_room.description} \n ")
            elif player.current_room.is_lit == False and not player.inventory.__contains__(item_list['lantern']):
                print(" \n It's pitch black. You need a source of light to see anything. \n ")
            elif len(player.current_room.monsters) > 0:
                if player.inventory.__contains__(item_list['sword']) and player.inventory.__contains__(item_list['shield']):
                    print(player.current_room.monsters[0].monster_death)
                    player.current_room.remove_monster(player.current_room.monsters[0])
                else:
                    print(player.current_room.monsters[0].player_kill)
                    running = False
        elif player.current_room.n_to != None and player.current_room.n_to.is_locked:
            print(" \n A locked door bars your way forward... You need a key to continue forward. \n ")
        else:
            print(notNorth)

    elif player_input == "a":
        if player.current_room.w_to != None and (not player.current_room.w_to.is_locked or player.inventory.__contains__(item_list['key'])):
            if player.inventory.__contains__(item_list['key']) and player.current_room.w_to.is_locked:
                print(" \n You used the key to open the locked door. \n ")
                player.current_room = player.current_room.w_to
                print(f" \n {player.current_room.description} \n ")
            elif player.current_room.is_lit == False and not player.inventory.__contains__(item_list['lantern']):
                print(" \n It's pitch black. You need a source of light to see anything. \n ")
            elif len(player.current_room.monsters) > 0:
                if player.inventory.__contains__(item_list['sword']) and player.inventory.__contains__(item_list['shield']):
                    print(player.current_room.monsters[0].monster_death)
                    player.current_room.remove_monster(player.current_room.monsters[0])
                else:
                    print(player.current_room.monsters[0].player_kill)
                    running = False
        elif player.current_room.w_to != None and player.current_room.w_to.is_locked:
            print(" \n A locked door bars your way forward... You need a key to continue forward. \n ")
        else:
            print(notWest)

    elif player_input == "d":
        if player.current_room.e_to != None and (not player.current_room.e_to.is_locked or player.inventory.__contains__(item_list['key'])):
            if player.inventory.__contains__(item_list['key']) and player.current_room.e_to.is_locked:
                print(" \n You used the key to open the locked door. \n ")
                player.current_room = player.current_room.e_to
                print(f" \n {player.current_room.description} \n ")
            elif player.current_room.is_lit == False and not player.inventory.__contains__(item_list['lantern']):
                print(" \n It's pitch black. You need a source of light to see anything. \n ")
            elif len(player.current_room.monsters) > 0:
                if player.inventory.__contains__(item_list['sword']) and player.inventory.__contains__(item_list['shield']):
                    print(player.current_room.monsters[0].monster_death)
                    player.current_room.remove_monster(player.current_room.monsters[0])
                else:
                    print(player.current_room.monsters[0].player_kill)
                    running = False
        elif player.current_room.e_to != None and player.current_room.e_to.is_locked:
            print(" \n A locked door bars your way forward... You need a key to continue forward. \n ")
        else:
            print(notEast)

    elif player_input == "s":
        if player.current_room.s_to != None and (not player.current_room.s_to.is_locked or player.inventory.__contains__(item_list['key'])):
            if player.inventory.__contains__(item_list['key']) and player.current_room.s_to.is_locked:
                print(" \n You used the key to open the locked door. \n ")
                player.current_room = player.current_room.s_to
                print(f" \n {player.current_room.description} \n ")
            elif player.current_room.is_lit == False and not player.inventory.__contains__(item_list['lantern']):
                print(" \n It's pitch black. You need a source of light to see anything. \n ")
            elif len(player.current_room.monsters) > 0:
                if player.inventory.__contains__(item_list['sword']) and player.inventory.__contains__(item_list['shield']):
                    print(player.current_room.monsters[0].monster_death)
                    player.current_room.remove_monster(player.current_room.monsters[0])
                else:
                    print(player.current_room.monsters[0].player_kill)
                    running = False
        elif player.current_room.s_to != None and player.current_room.s_to.is_locked:
            print(" \n A locked door bars your way forward... You need a key to continue forward. \n ")
        else:
            print(notSouth)

    elif player_input == "i":
        if len(player.inventory) > 0:
            for index, item in enumerate(player.inventory):
                print("")
                for item in player.inventory:
                    print(f"{item.name}")
                inv_input = input(" \n Write the name of the item you would like to drop or write 'CLOSE' to close your inventory: \n ").lower()
                if inv_input != "close" and player.inventory.__contains__(item_list[inv_input]):
                    print(f" \n You dropped the {item_list[inv_input].name}. \n ")
                    player.current_room.add_item(item_list[inv_input])
                    player.drop_from_inventory(item_list[inv_input])
                elif inv_input == "close":
                    print(" \n You closed your inventory. \n ")
                else: 
                    print(" \n Please enter valid command. \n ")
        else:
            print(" \n Your inventory is empty. \n ")

    elif player_input == "o":
        if len(player.current_room.items) > 0 and (player.current_room.is_lit or player.inventory.__contains__(item_list['lantern'])):
            print("")
            for item in player.current_room.items:
                print(f"{item.name}: {item.description}")
                search_input = input(" \n Write the name of the item you would like to pick up or write 'STOP' to stop searching: \n ")
                if search_input != "stop" and player.current_room.items.__contains__(item_list[search_input]):
                    print(f" \n You picked up the {item_list[search_input].name}. \n ")
                    player.current_room.remove_item(item_list[search_input])
                    player.add_to_inventory(item_list[search_input])
                elif search_input == "stop":
                    print(" \n You decided to stop searching the room. \n ")
                else:
                    print (" \n Please enter valid command. \n ")
        elif player.current_room.is_lit == False and not player.inventory.__contains__(item_list['lantern']):
            print(" \n It is too dark to see anything. \n ")
        else:
            print(" \n You searched the room but didn't find anything of use. \n ")

    elif player_input == "q":
        running = False
        print(" \n Thank you for playing. \n ")

    else:
        print(" \n Please enter valid command. \n ")