#!/usr/bin/python3

# print a main menu and the commands
def showInstructions():
    print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
  teleport [roomname]
''')


# player cannot teleport to current room and the garden
def showTeleportRoom():
    teleportRoom = []
    for room in rooms:
        if room not in [currentRoom, 'Garden']:
            teleportRoom.append(room)
    return teleportRoom


def showStatus():
    # print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    # print the current inventory
    print('Inventory : ' + str(inventory))
    # print an item if there is one
    if 'item' in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
    # print directions
    direction = ''
    for key in rooms[currentRoom]:
        if key != "item":
            direction += f"{key.title()} to {rooms[currentRoom][key]}. "
    print(direction)
    # print the rooms users can teleport
    teleportRoom = showTeleportRoom()
    print(f"You can teleport to {teleportRoom}")
    print("---------------------------")


# an inventory, which is initially empty
inventory = []

# a dictionary linking a room to other rooms
rooms = {

    'Hall': {
        'south': 'Kitchen',
        'east': 'Dining Room',
        'west': 'Library',
        'item': 'key'
    },

    'Kitchen': {
        'north': 'Hall',
        'item': 'monster',
    },
    'Dining Room': {
        'west': 'Hall',
        'south': 'Garden',
        'item': 'potion',
        'north': 'Pantry',
    },
    'Garden': {
        'north': 'Dining Room'
    },
    'Pantry': {
        'south': 'Dining Room',
        'item': 'cookie',
    },
    'Library': {
        'east': 'Hall',
        'south': 'Attic',
        'item': 'book'
    },
    'Attic': {
        'north': 'Library',
        'item': 'secret'
    }
}

# start the player in the Hall
currentRoom = 'Hall'


# loop forever
while True:

    showInstructions()
    showStatus()
    move = ''
    while move == '':
        move = input('>')
    # handle empty input
    if move == '':
        continue
    move = move.lower().split(" ", 1)
    # handle invalid command
    if len(move) == 1:
        continue
    # if they type 'go' first
    if move[0] == 'go':
        # check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            # set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        # there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    # if they type 'get' first
    if move[0] == 'get':
        # if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            # add the item to their inventory
            inventory += [move[1]]
            # display a helpful message
            print(move[1] + ' got!')
            # delete the item from the room
            del rooms[currentRoom]['item']
        # otherwise, if the item isn't there to get
        else:
            # tell them they can't get it
            print('Can\'t get ' + move[1] + '!')

    # if they type 'teleport' first
    if move[0] == 'teleport':
        teleportRoom = showTeleportRoom()
        if move[1].title() in teleportRoom:
            currentRoom = move[1].title()
        else:
            print(f'Can\'t teleport to {move[1].title()}.')

    # allow user to see secret only when they are in the attic with secret
    if move[0] == 'read' and currentRoom == 'Attic' and 'secret' in inventory:
        print('Here is the secret: The exit is in the Garden. The potion is in the dining room and the key is in the Hall and you need both to escape. One more thing, there is a monster in the kitchen, don\' go there!')
    # instruct the user how to use secret
    if currentRoom == 'Attic' and 'secret' not in inventory:
        print('Get the secret first and then use secret command "read secret" to see it!')
    # instruct the user how to win the game
    if currentRoom == 'Garden' and ('key' not in inventory or 'potion' not in inventory):
        print('You are almost there, you need a key and potion to escape! Go find it')
    # Define how a player can win
    if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
        break

    # If a player enters a room with a monster
    elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you... GAME OVER!')
        break
