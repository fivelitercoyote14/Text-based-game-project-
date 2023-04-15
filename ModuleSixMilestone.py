# Emilio Acuna-Reyes


# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'South': 'Bedroom'},
    'Bedroom': {'North': 'Great Hall', 'East': 'Cellar'},
    'Cellar': {'West': 'Bedroom'}
}
# Initialize the game state.
current_room = 'Great Hall'


# Create a function to display the current room.
def display_room(room):
    print(f"You are currently in the {room}.")


# a function to process user input and move between rooms or exit the game.
def process_input(user_input, current_room):
    if user_input.lower() == 'exit':
        return 'exit'
    elif user_input.capitalize() in rooms[current_room]:
        new_room = rooms[current_room][user_input.capitalize()]
        return new_room
    else:
        print("Invalid command. Please try again.")
        return current_room


# main game loop
while current_room != 'exit':
    display_room(current_room)
    user_input = input("Enter a direction (North, South, East, West) or type 'exit' to quit: ")
    current_room = process_input(user_input, current_room)

print("You have exited the game.")
