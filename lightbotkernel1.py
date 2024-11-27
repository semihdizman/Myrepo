# This is an editing for the final part of the lightbot kernel

# Global variables for bot's state
bot_position = [0, 9]  # Start at [0, 9]
bot_direction = 'E'  # Facing East initially (N, E, S, W)
grid_size = 10  # Grid size (10x10)

# Example terrain: each cell is a dictionary with "light" status
terrain = [
    [{'light': 0} for _ in range(grid_size)]
    for _ in range(grid_size)
]

# Function to toggle the light at the bot's current position
def toggle_light():
    global terrain, bot_position
    x, y = bot_position
    if terrain[y][x]['light'] == 0:
        terrain[y][x]['light'] = 1
        print(f"Toggled light ON at ({x}, {y}).")
    else:
        print(f"Light at ({x}, {y}) is already ON. Cannot toggle OFF.")

# Function to turn the bot right (90 degrees)
def turn_right():
    global bot_direction
    directions = ['N', 'E', 'S', 'W']
    if bot_direction in directions:
        current_idx = directions.index(bot_direction)
        bot_direction = directions[(current_idx + 1) % 4]
    else:
        print(f"Error: Invalid bot direction '{bot_direction}'.")

# Function to turn the bot left (90 degrees)
def turn_left():
    global bot_direction
    directions = ['N', 'E', 'S', 'W']
    if bot_direction in directions:
        current_idx = directions.index(bot_direction)
        bot_direction = directions[(current_idx - 1) % 4]
    else:
        print(f"Error: Invalid bot direction '{bot_direction}'.")

# Function to check if the bot can move to a neighboring square
def can_move(new_x, new_y, allow_jump=False):
    global terrain, bot_position, grid_size
    if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
        return True
    else:
        print(f"Invalid position: ({new_x}, {new_y}) is out of bounds.")
    return False

# Function to move the bot forward in the direction it is facing
def move_forward(allow_jump=False):
    global bot_position, bot_direction
    new_x, new_y = bot_position[0], bot_position[1]

    if bot_direction == 'N':
        new_y -= 1
    elif bot_direction == 'E':
        new_x += 1
    elif bot_direction == 'S':
        new_y += 1
    elif bot_direction == 'W':
        new_x -= 1
    else:
        print(f"Error: Unknown direction '{bot_direction}'.")
        return

    if can_move(new_x, new_y, allow_jump):
        bot_position[0], bot_position[1] = new_x, new_y
        print(f"Moved to ({new_x}, {new_y}).")
    else:
        print(f"Cannot move to ({new_x}, {new_y}).")

# Function to execute a sequence of instructions
def execute_instructions(instructions):
    for instr in instructions:
        if instr == '^':
            move_forward()  # Normal move
        elif instr == '*':
            move_forward(allow_jump=True)  # Jump to a higher square
        elif instr == '>':
            turn_right()
        elif instr == '<':
            turn_left()
        elif instr == '@':
            toggle_light()
        else:
            print(f"Unknown instruction: '{instr}'")
        print_state()  # Print the state after each step

# Function to print the current state of the bot and the terrain
def print_state():
    global bot_position, bot_direction, terrain
    print(f"Bot Position: {bot_position}, Direction: {bot_direction}")
    print("Lit squares:")
    for row in terrain:
        print([cell['light'] for cell in row])
# Example: You can manually set the heights of squares here, just for simplicity ill do the following
terrain[9][9]['height'] = 0
terrain[9][8]['height'] = 0
terrain[8][9]['height'] = 0

# Example: Execute the provided instruction sequence
# Litting up the squares in the shape of number 3 as I did in my previous homeworks to check if the code is correct.
if __name__ == "__main__":
    instructions = "^<^@^@>^>^@^<^@^@^<^@>^@^<^@^@<^@>^@<^@^@>^>^^@^@<^@^<^@^@>^<^@^@^<^@>^@<^@^^^^^^<^^^^^^"
    execute_instructions(instructions)