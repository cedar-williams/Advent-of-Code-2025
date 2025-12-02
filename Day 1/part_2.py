# --- Day 1: Secret Entrance ---

def dial_spin_zero_count(start, dir, mv) -> int:
    num_zeros = 0
    cur_dial_num = start

    if dir == "R":
        for x in range(mv):
            cur_dial_num += 1
            if cur_dial_num == 100:
                cur_dial_num = 0
            if cur_dial_num == 0:
                num_zeros += 1
    else:
        for x in range(mv):
            cur_dial_num -= 1
            if cur_dial_num == -1:
                cur_dial_num = 99
            if cur_dial_num == 0:
                num_zeros += 1

    return num_zeros

# Import the file
with open("input.txt") as f:
    file_contents = [line.strip() for line in f]

# Turn the dial for each line
zero_count = 0
current_position = 50 # Dial starts at 50

for turn in file_contents:

    direction, mv_amt = turn[0], int(turn[1:])

    zero_count += dial_spin_zero_count(current_position, direction, mv_amt)

    # Turn dial right, plus
    if direction == 'R':
        current_position = (current_position + mv_amt) % 100

    # Turn dial left, minus
    else:
        current_position = (current_position - mv_amt) % 100


print(f'Door password: {zero_count}')