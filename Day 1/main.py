# --- Day 1: Secret Entrance ---

# Import the file
file_contents = []
with open("input.txt") as f:
    file_contents = [line.strip() for line in f]

# Turn the dial for each line
zero_count = 0
current_position = 50 # Dial starts at 50

for turn in file_contents:

    direction, number = turn[0], int(turn[1:])

    # Turn dial right, plus
    if direction == 'R':
        current_position = (current_position + number) % 100

    # Turn dial left, minus
    else:
        current_position = (current_position - number) % 100

    if current_position == 0:
        zero_count += 1

print(f'Door password: {zero_count}')