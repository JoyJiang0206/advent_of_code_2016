# Starting Condition
position_x, position_y = 0, 0
current_direction = 'N'

visited_positions = []  # List of positions (x, y)
found_hq = False

#Process
direction_map = {
    #e.g. Facing North: if I turn Left I face West, if I turn Right I face East
    'N': {'L': 'W', 'R': 'E'},
    'E': {'L': 'N', 'R': 'S'},
    'S': {'L': 'E', 'R': 'W'},
    'W': {'L': 'S', 'R': 'N'}
}

coordinate_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

# Read Input from File
with open('day_01.txt', 'r') as file_obj:
    input_text = file_obj.read()

# Sample Input
for instruction in input_text.split(', '):
    left_right = instruction[0]    #'L' or 'R'
    step_text = instruction[1:]    # 'x'
    steps = int(step_text)

    # Execute the Input - Part 1
    new_direction = direction_map[current_direction][left_right]
    # if new_direction == 'N':
    #     position_y = position_y + steps    # Go North
    # elif new_direction == 'S':
    #     position_y = position_y - steps    # Go South
    # elif new_direction == 'E':
    #     position_x = position_x + steps    # Go East
    # elif new_direction == 'W':
    #     position_x = position_x - steps    # Go West
    # else:
    #     print (f'Wrong direction: {new_direction}')

    # Execute the Input - Part 2
    coordinate_adjustment = coordinate_map[new_direction]
    for step in range(steps):
        x_adjustment, y_adjustment = coordinate_adjustment
        position_x = position_x + x_adjustment
        position_y = position_y + y_adjustment
        # If position was visited, break the loop to print result
        if (position_x, position_y) in visited_positions:
            found_hq = True
            break
        visited_positions.append((position_x, position_y))
    if found_hq:
        break
# Record the new direction
    current_direction = new_direction

# Print Result
print (f'Ending position: ({position_x}, {position_y})')
print (f'Distance: {abs(position_x) + abs(position_y)}')