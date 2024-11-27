#This is the old version of the code
# Initialize the terrain and bot state
grid_size = 10  # 10x10 grid
terrain = [[{'height': 0, 'light': 0} for _ in range(grid_size)] for _ in range(grid_size)]  # Store height and light state
bot_position = [9, 0]  # Bot starts at the bottom-left corner
bot_direction = 'E'  # Bot starts facing EAST

# Function to print the current state
def print_state():
    print(f"Bot Position: {bot_position}, Facing: {bot_direction}")
    for row in terrain:
        print([f"H:{cell['height']} L:{cell['light']}" for cell in row])

# Function to turn the bot right (90 degrees)
def turn_right():
    global bot_direction
    directions = ['N', 'E', 'S', 'W']
    current_idx = directions.index(bot_direction)
    bot_direction = directions[(current_idx + 1) % 4]

# Function to turn the bot left (90 degrees)
def turn_left():
    global bot_direction
    directions = ['N', 'E', 'S', 'W']
    current_idx = directions.index(bot_direction)
    bot_direction = directions[(current_idx - 1) % 4]

# Function to check if the bot can move to a neighboring square
def can_move(new_x, new_y, allow_jump=False):
    current_height = terrain[bot_position[1]][bot_position[0]]['height']
    if 0 <= new_x < grid_size and 0 <= new_y < grid_size:
        next_height = terrain[new_y][new_x]['height']
        # The bot can move if the height difference is 0 or it can jump if the height difference is exactly 1 and jump is allowed
        if next_height == current_height or (allow_jump and next_height == current_height + 1):
            return True
    return False

# Function to move the bot forward in the direction it is facing
def move_forward():
    global bot_position
    if bot_direction == 'N' and bot_position[1] > 0:
        bot_position[1] -= 1  # Move up (within bounds)
    elif bot_direction == 'E' and bot_position[0] < grid_size - 1:
        bot_position[0] += 1  # Move right (within bounds)
    elif bot_direction == 'S' and bot_position[1] < grid_size - 1:
        bot_position[1] += 1  # Move down (within bounds)
    elif bot_direction == 'W' and bot_position[0] > 0:
        bot_position[0] -= 1  # Move left (within bounds)


# Function to toggle the light at the bot's current position
def toggle_light():
    x, y = bot_position
    terrain[y][x]['light'] = 1 - terrain[y][x]['light']  # Toggle between 0 (off) and 1 (lit)

# Function to execute a series of instructions
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
        print_state()  # Print the state after each step

# Example: You can manually set the heights of squares here, just for simplicity ill do the following
terrain[9][9]['height'] = 0
terrain[9][8]['height'] = 0
terrain[8][9]['height'] = 0

# Execute the instructions I did for the last homework
instructions = "^<^@^@>^>^@^<^@^@^<^@>^@^<^@^@<^@>^@<^@^@>^>^^@^@<^@^<^@^@>^<^@^@^<^@>^@<^@^^^^^^<^^^^^^"
execute_instructions(instructions)

# Function to print the final matrix of lit squares (1 for lit, 0 for unlit)
def print_lit_squares():
    print("Final lit-up squares (1 = lit, 0 = unlit):")
    for row in terrain:
        print([cell['light'] for cell in row])

# Print the final state of the lit-up squares
print_lit_squares()
