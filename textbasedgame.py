# Emilio Acuna-Reyes

# room dictionary
rooms = {
    'Entrance': {'West': 'Central Hub'},
    'Central Hub': {'Northwest': 'Crypt', 'North': 'Library', 'Northeast': 'Fiery Forge', 'Southeast': 'Enchanted '
                                                                                                       'Garden',
                    'South': 'Ice Cavern', 'East': 'Throne Room'},
    'Crypt': {'Southeast': 'Central Hub'},
    'Library': {'South': 'Central Hub'},
    'Fiery Forge': {'Southwest': 'Central Hub'},
    'Enchanted Garden': {'Northwest': 'Central Hub'},
    'Ice Cavern': {'North': 'Central Hub'},
    'Throne Room': {'West': 'Central Hub'}
}

# define actions the player can take
available_actions = {
    'Entrance': ['Go West'],
    'Central Hub': ['Go Northwest', 'Go North', 'Go Northeast', 'Go Southeast', 'Go South', 'Go East', 'Collect Item'],
    'Crypt': ['Go Southeast', 'Collect Item'],
    'Library': ['Go South', 'Collect Item'],
    'Fiery Forge': ['Go Southwest', 'Collect Item'],
    'Enchanted Garden': ['Go Northwest', 'Collect Item'],
    'Ice Cavern': ['Go North', 'Collect Item'],
    'Throne Room': ['Go West', "defeat malazar"]
}


# Define the game state (class)
class GameState:
    def __init__(self):
        self.inventory = {}
        self.current_room = 'Entrance'


game_state = GameState()


# display room descriptions
def display_room_description(room):
    descriptions = {
        'Entrance': "You are at the entrance of a mysterious cave.",
        'Central Hub': "You are in the central hub, with paths leading in various directions.",
        'Crypt': "You are in a crypt teeming with undead creatures.",
        'Library': "You are in a library filled with magical secrets.",
        'Fiery Forge': "You are in a fiery forge guarded by a mythical blacksmith.",
        'Enchanted Garden': "You are in an enchanted garden flourishing with otherworldly flora and fauna.",
        'Ice Cavern': "You are in a treacherous ice cavern.",
        'Throne Room': "You are in Malazar's throne room."
    }
    print(descriptions[room])


# display actions function
def display_available_actions(room):
    actions = available_actions.get(room)
    if actions:
        print("Available actions:")
        for action in actions:
            print(f"- {action}")
    else:
        print("There are no available actions.")


# define the function for user input
def process_user_input(user_input, game_state):
    user_input = user_input.lower()

    # Check for movement input
    for room_action, room_name in rooms[game_state.current_room].items():
        if user_input == f"go {room_action.lower()}":
            game_state.current_room = move_between_rooms(game_state.current_room, room_action)
            return True

    # Check for defeat Malazar input
    if user_input == "defeat malazar":
        defeat_malazar(game_state)
        return True

    # Check for item collection input
    if user_input == "collect item":
        collect_item(game_state)
        return True

    return False


# define function to win the game
def defeat_malazar(game_state):
    RED_TEXT = "\033[31m"
    RESET_TEXT = "\033[0m"

    if game_state.current_room == 'Throne Room' and all(game_state.inventory.values()):
        print("Congratulations! You have collected all six artifacts and defeated Malazar, saving the village.")
        exit(0)
    else:
        print(RED_TEXT + "You cannot defeat Malazar without all six artifacts. You were not able to save the village. "
                         "Game over." + RESET_TEXT)


# define the function to move the player between rooms
def move_between_rooms(current_room, direction):
    if direction in rooms[current_room]:
        new_room = rooms[current_room][direction]
        return new_room
    else:
        print("You cannot move in that direction.")
        return current_room


# define the function to allow the player to collect the item
def collect_item(game_state):
    room_items = {
        'Crypt': 'Orb of Light',
        'Library': 'Staff of the Ancients',
        'Fiery Forge': 'Tome of Shadows',
        'Enchanted Garden': 'Phoenix Feather',
        'Ice Cavern': 'Crystal of Eternity',
        'Central Hub': 'Amulet of the Elements'
    }

    current_room = game_state.current_room
    if room_items.get(current_room):
        item_name = room_items[current_room]
        if item_name not in game_state.inventory:
            game_state.inventory[item_name] = True
            print(f"You have collected the {item_name}.")
        else:
            print("You have already collected the item in this room.")
    else:
        print("There is no item in this room.")


# display user inventory
def display_inventory(game_state):
    print("Inventory:")
    if game_state.inventory:
        for item, collected in game_state.inventory.items():
            if collected:
                print(f"- {item}")
    else:
        print("Your inventory is empty.")


# main function
def main():
    game_state = GameState()

    while True:
        display_room_description(game_state.current_room)
        display_available_actions(game_state.current_room)
        user_input = input("What would you like to do? ").lower()

        if user_input == "exit":
            print("You have decided to exit the game. Goodbye!")
            break

        input_valid = process_user_input(user_input, game_state)

        if not input_valid:
            print("Invalid input, please try again.")

        display_inventory(game_state)

        # Check for win or loss conditions
        if game_state.current_room == 'Throne Room':
            if len(game_state.inventory) == 6:  # Assuming the player needs all 6 items
                print("Congratulations! You have collected all six artifacts and defeated Malazar, saving the village.")
                break
            else:
                print(
                    "You entered Malazar's throne room without all six artifacts. Malazar easily defeats you. Game "
                    "over.")
                break
        elif game_state.current_room == 'Exit':  # Assuming there's an exit option to end the game
            print("You decided to exit the game. Thanks for playing!")
            break


if __name__ == "__main__":
    main()
