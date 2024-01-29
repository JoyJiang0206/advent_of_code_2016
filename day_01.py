# Starting Condition
position_x, position_y = 0, 0
current_direction = 'N'

#Process
direction_map = {
    #e.g. Facing North: if I turn Left I face West, if I turn Right I face East
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'}
}

# Read Input from File
with open('day_01.txt', 'r') as file_obj:
    input_text = file_obj.read()

# Sample Input
for instruction in input_text.split(', '):
    left_right = instruction[0]    #'L' or 'R'
    step_text = instruction[1:]    # 'x'
    steps = int(step_text)

    # Execute the Input
    new_direction = direction_map[current_direction][left_right]
    if new_direction == 'N':
        position_y = position_y + steps    # Go North
    elif new_direction == 'S':
        position_y = position_y - steps    # Go South
    elif new_direction == 'E':
        position_x = position_x + steps    # Go East
    elif new_direction == 'W':
        position_x = position_x - steps    # Go West
    else:
        print (f'Wrong direction: {new_direction}')
# Record the new direction
    current_direction = new_direction

# Print Result
print (f'Ending position: ({position_x}, {position_y})')
print (f'Distance: {abs(position_x) + abs(position_y)}')