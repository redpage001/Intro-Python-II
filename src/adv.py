from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
    'sword': Item("Sword", "You've found a steel sword on the ground. It could be handly along the way."),
    'shield': Item("Shield", "You found an iron shield lying against the wall. It looks well worn but sturdy."),
    'key': Item("Mysterious Key", "You found an old key. It looks to be very important.")
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#Fill rooms with items

room['foyer'].add_item(item['sword'])
room['overlook'].add_item(item['key'])
room['narrow'].add_item(item['shield'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input(" \n Enter Player Name here: \n ")
player = Player(player_name, room['outside'])

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
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            print(f" \n {player.current_room.description} \n ")
        else:
            print(notNorth)

    elif player_input == "a":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            print(f" \n {player.current_room.description} \n ")
        else:
            print(notWest)

    elif player_input == "d":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            print(f" \n {player.current_room.description} \n ")
        else:
            print(notEast)

    elif player_input == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            print(f" \n {player.current_room.description} \n ")
        else:
            print(notSouth)

    elif player_input == "i":
        if len(player.inventory) > 0:
            for index, item in enumerate(player.inventory):
                print(f"{index}: {item.name}")
                inv_input = input(" \n Type in slot number to remove selected item or type 'No' to close inventory: \n")
                if inv_input == "No":
                    print(" \n You closed your inventory. \n")
                elif inv_input == "0" or inv_input == "1" or inv_input == "2":
                    print(f"\n you dropped the {player.inventory[int(inv_input)]}. \n ")
                    room[player.current_room.name].add_item(player.inventory[int(inv_input)])
                    player.drop_from_inventory(int(inv_input))
                else:
                    print(" \n Please enter valid command. \n ")
        else:
            print(" \n Your inventory is empty. \n ")

    elif player_input == "o":
        if len(player.current_room.items) > 0:
            for index, item in enumerate(player.current_room.items):
                print(f" \n {item.description} \n ")
                search_input = input(f" \n Would you like to pick up the {item.name} \n YES/NO \n ")
                if search_input == "YES":
                    player.add_to_inventory(player.current_room.items[int(index)])
                    room[player.current_room.name].remove_item(index)
                    print(f" \n You picked up the {player.inventory[int(index)]} \n ")
        else:
            print(" \n You don't find anything. \n ")

    elif player_input == "q":
        running = False
        print(" \n Thank you for playing. \n ")
        
    else:
        print(" \n Please enter valid command. \n ")