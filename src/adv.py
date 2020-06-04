from room import Room
from player import Player
from item import Item

# manufacturing some Items
item = {
    "torch": Item("torch", "This may help you see somethign you've overlooked"),
    "watch": Item("watch", "Don't lose track of time in the cave"),
    "cat": Item("cat", "Meet your new cat Kimby. She hungry for gold...sometimes"),
    "sword": Item("sword", "A keen edge to keep the cave swine in line")
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item["watch"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [item["torch"], item["cat"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["sword"]]),

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



# put items in the rooms
# room['outside'].room_items = [item["watch"]]
# room['overlook'].room_items = [item["torch"], item["cat"]]
# room['narrow'].room_items = [item["sword"]]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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


def game():
    username = input("Please provide your characters name: ")
    first_room = room['outside']
    player = Player(username, first_room)

    print(f"\n    Hello {player}, you are ")
    # print(
    #     f"        {player.current_room.name}. {player.current_room.description}\n\n")
        ################################
    print(player.player_room())
    move = input(
        "Please select a direction to move and then press [enter]: \n [n] North | [s] South | [e] East | [w] West | [q] quit \n").lower()

    while player.victory == False:
        if move == "q":
            print("\n You'll never reach the treasure now! Bye forever. \n")
            exit()
        try:
            if move == "n":
                player.set_location(player.current_room.n_to)
                
            elif move == "s":
                player.set_location(player.current_room.s_to)
               
            elif move == "e":
                player.set_location(player.current_room.e_to)
                
            elif move == "w":
                player.set_location(player.current_room.w_to)
                
            else:
                # incorrect direction value, throw error
                raise ValueError

        except ValueError:
            print("\n !!! Select a valid direction !!!")

        except:
            print("\n !!! There is nowhere to move in this direction !!! \n")

        print(f"\n    {player}, you are in the")
        # print(
        #     f"        {player.current_room.name}. {player.current_room.description} \n")
        print(player.player_room())

        # print({player.current_room.room_items})
        # for when player reaches end of game
        if player.current_room == room['treasure']:
            print("\nCongratulations, you have reached the end of the game!\n")
            exit()
        # reassign the move variable before next loop starts
        move = input(
            "Please select a direction to move and then press [enter]: \n [n] North | [s] South | [e] East | [w] West | [q] quit \n\n").lower()

game()
