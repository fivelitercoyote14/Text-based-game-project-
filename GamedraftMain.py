# Emilio Acuna
import random

# Define rooms and their connections
rooms = {
    "entrance": {"north": "central_area"},
    "central_area": {"north": "crypt", "east": "library", "south": "entrance", "west": "forge"},
    "crypt": {"south": "central_area"},
    "library": {"west": "central_area"},
    "forge": {"east": "central_area"},
    # Add other rooms here
}


game_state = {
    'current_room': 'entrance',
    'inventory': [],
    'game_over': False
}


def display_room(room):
    # Add room descriptions and available actions
    room_data = {
        'entrance': {
            'description': 'You are at the entrance of the mysterious land of Eldaria.',
            'actions': ['move']
        },
        # Add other room descriptions and actions
    }

    print(room_data[room]['description'])
    print("Available actions:", ", ".join(room_data[room]['actions']))
""" FIXME
def move(current_room):
    
    # Use the rooms dictionary provided earlier to update the player's current room
    # Implement the move logic and update game_state

def interact(current_room):
    # Implement interaction logic based on the current room and update game_state

def collect_item(current_room):
    # Implement item collection logic based on the current room and update game_state
    """



def inspect_chest():
    print("You inspect the chest and find a hidden compartment.")
    print("You obtain the magical item!")
    # Add the item to the player's inventory or update the game state


def defeat_mob():
    print("You engage the low-level mob in combat.")
    # Implement combat mechanics, for example, randomize the outcome
    outcome = random.choice(["victory", "defeat"])

    if outcome == "victory":
        print("You have defeated the low-level mob!")
        print("You obtain the magical item!")
        # Add the item to the player's inventory or update the game state
    else:
        print("You have been defeated by the low-level mob.")
        # Handle player defeat, e.g., respawn or end the game


# Initialize player's starting location
current_room = "entrance"

# Main game loop
while True:
    # Print current room description
    print(f"You are in the {current_room}")

    # Get user input for direction
    direction = input("Enter a direction (north, east, south, west) or 'quit' to exit: ").lower()

    # Check if user wants to quit
    if direction == "quit":
        print("Goodbye!")
        break

    # Check if the direction is valid
    if direction in rooms[current_room]:
        # Update the current room
        current_room = rooms[current_room][direction]
    else:
        # If direction is invalid, print an error message
        print("You cannot go in that direction.")
# Print a description of the room
    print("You enter a room and see a mysterious chest and a low-level mob guarding it.")

    # Get user input for their choice
    choice = input("Do you want to 'inspect' the chest or 'defeat' the mob? Type 'quit' to exit: ").lower()

    # Check if the user wants to quit
    if choice == "quit":
        print("Goodbye!")
        break

    # Handle the user's choice
    if choice == "inspect":
        inspect_chest()
        break
    elif choice == "defeat":
        defeat_mob()
        break
    else:
        print("Invalid choice. Please try again.")


def move(param):
    pass


while not game_state['game_over']:
    display_room(game_state['current_room'])
    user_input = input("What would you like to do? ")
    # Process user input, call the appropriate action function, and update game_state

    # Example:
    if user_input == "move":
        move(game_state['current_room'])
    # Add other actions and their corresponding function calls