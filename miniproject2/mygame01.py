#!/usr/bin/python3
"""Driving a simple game framework with
   a dictionary object | Alta3 Research"""

import roomsfile

def show_instructions():
    """Show the game instructions when called."""
    print('''
    RPG Game
    ========
    Get to the Garden with a key and a potion to win! Avoid the monsters!
    Commands:
      go [direction]
      get [item]
      look
      inventory
    ''')

def show_status():
    """Determine the current status of the player."""
    print('---------------------------')
    print(f'You are in the {current_room}')
    print(f'Inventory: {inventory}')
    if "item" in rooms[current_room]:
        print(f'You see a {rooms[current_room]["item"]}')
    print('---------------------------')

def describe_room(room):
    """Generate and return the available directions from the room."""
    # Create a list to store the direction descriptions
    direction_list = []

    # Check each possible direction and add to the list if it exists
    if "north" in rooms[room]:
        direction_list.append("north")
    if "south" in rooms[room]:
        direction_list.append("south")
    if "east" in rooms[room]:
        direction_list.append("east")
    if "west" in rooms[room]:
        direction_list.append("west")
    if "up" in rooms[room]:
        direction_list.append("up")
    if "down" in rooms[room]:
        direction_list.append("down")

    # Join the list into a single string
    directions = ", ".join(direction_list)
    
    # Create the final description string
    return f'You can go: {directions}.'

# An inventory, which is initially empty
inventory = []

# Load rooms data from the external Python file
rooms = roomsfile.rooms

# Start the player in the Hall
current_room = 'Hall'

show_instructions()

# Breaking this while loop means the game is over
while True:
    show_status()
    
    # The player MUST type something in
    # otherwise input will keep asking
    move = ''
    while move == '':
        move = input('>')

    # Normalizing input:
    # .lower() makes it lower case, .split() turns it to a list
    # therefore, "get golden key" becomes ["get", "golden key"]
    move = move.strip().lower().split(" ", 1)

    # If they type 'go' first
    if move[0] == 'go':
        # Check that they are allowed wherever they want to go
        if move[1] in rooms[current_room]:
            # Set the current room to the new room
            current_room = rooms[current_room][move[1]]
        # If they aren't allowed to go that way:
        else:
            print('You can\'t go that way!')

    # If they type 'get' first
    elif move[0] == 'get':
        # Make two checks:
        # 1. if the current room contains an item
        # 2. if the item in the room matches the item the player wishes to get
        if "item" in rooms[current_room] and move[1] in rooms[current_room]['item']:
            # Add the item to their inventory
            inventory.append(move[1])
            # Display a helpful message
            print(f'{move[1]} got!')
            # Delete the item key:value pair from the room's dictionary
            del rooms[current_room]['item']
        # If there's no item in the room or the item doesn't match
        else:
            # Tell them they can't get it
            print(f'Can\'t get {move[1]}!')

    # If they type 'look'
    elif move[0] == 'look':
        print(describe_room(current_room))

    # If they type 'inventory'
    elif move[0] == 'inventory':
        print(f'Inventory: {inventory}')


    # If a player enters a room with a monster
    if 'item' in rooms[current_room] and 'monster' in rooms[current_room]['item']:
        if 'shield' in inventory:
            print('You use your shield to fend off the monster and escape back to the Hall!')
            current_room = 'Hall'
        else:
            print('A monster has got you... GAME OVER!')
            break

    # Define how a player can win
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

