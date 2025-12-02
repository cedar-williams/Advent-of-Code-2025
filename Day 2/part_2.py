# --- Day 2: Gift Shop ---
import math

# Ingest input
with open("input.txt") as f:
    id_ranges = f.read().split(",")

# Locate invalid IDs
invalid_id_sum = 0

for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]

    # Check through range of ID's
    for cur_id in range(start, end + 1):

        # Check each possible length of repeat from 1 char repeating to 1/2 the num string vs the other half
        max_group_size = math.ceil(len(str(cur_id)) / 2)

        # For each possible group size for current id
        for size in range(1, max_group_size + 1):

            num_groups = math.ceil(len(str(cur_id)) / size)

            # Split number into arbitrary num of elements, ea. of len i
            split_nums = []
            for i in range(num_groups):
                split_nums.append(str(cur_id)[ size * i : (size * i) + size])

            # If all elements in the split num list are the same add to id_sum and exit early
            if all(x == split_nums[0] for x in split_nums) and (len(split_nums) > 1):
                invalid_id_sum += cur_id
                break

print(f'Sum of invalid IDs: {invalid_id_sum}')
