from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_name = input("Enter Player Name here:\n")
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
    player_input = input('\nUse "w" key to move North, "a" key to move West, "d" key to move East, "s" key to move South, and "q" key to quit game.\n')
    notNorth = "\n=============================================\n\n There is no path to the North.\n\n"
    notWest = "\n=============================================\n\n There is no path to the West.\n\n"
    notEast = "\n=============================================\n\n There is no path to the East.\n\n"
    notSouth = "\n=============================================\n\n There is no path to the South.\n\n"

    if player_input == "w":
        if player.current_room.n_to != None:
            player.current_room = player.current_room.n_to
            print(f"\n=============================================\n\n {player.current_room.description} \n\n")
        else:
            print(notNorth)
    elif player_input == "a":
        if player.current_room.w_to != None:
            player.current_room = player.current_room.w_to
            print(f"\n=============================================\n\n {player.current_room.description} \n\n")
        else:
            print(notWest)
    elif player_input == "d":
        if player.current_room.e_to != None:
            player.current_room = player.current_room.e_to
            print(f"\n=============================================\n\n {player.current_room.description} \n\n")
        else:
            print(notEast)
    elif player_input == "s":
        if player.current_room.s_to != None:
            player.current_room = player.current_room.s_to
            print(f"\n=============================================\n\n {player.current_room.description} \n\n")
        else:
            print(notSouth)
    elif player_input == "q":
        running = False
        print("\n========================================\n\n Thank you for playing.\n\n")
    else:
        print("\n========================================\n\n Please enter valid command\n\n")