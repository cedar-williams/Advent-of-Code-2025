# --- Day 2: Gift Shop ---

# Ingest input
with open("input.txt") as f:
    id_ranges = f.read().split(",")

# Locate invalid IDs
invalid_id_sum = 0

for id_range in id_ranges:
    start, end = [int(x) for x in id_range.split("-")]

    # Check through range of ID's
    for cur_id in range(start, end + 1):

        # Only check on even length numbers, odds can't be an invalid ID
        if len(str(cur_id)) % 2 == 0:
            mid_point = int(len(str(cur_id)) / 2)
            front, rear = str(cur_id)[0:mid_point], str(cur_id)[mid_point:]

            if front == rear:
                invalid_id_sum += cur_id

print(f'Sum of invalid IDs: {invalid_id_sum}')
