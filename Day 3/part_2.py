# --- Day 3: Lobby ---

# Import battery banks
with open("input.txt") as file:
    banks = [line.strip() for line in file]

# Find max joltage for each bank
total_joltage = 0
end_batt_size = 12 # How man batteries will be picked for the final battery banks

for bank in banks:

    batt_picks = [0 for x in range(end_batt_size)]
    bank_length = len(bank)

    for index, battery in enumerate(map(int, bank)):

        # Determine possible battery locations in output selection,
        #   offset from each side because batteries must be in order
        min_pos = 0 if (index <= bank_length - end_batt_size) else (index - (bank_length - end_batt_size))
        max_pos = index if (index < bank_length - (bank_length - end_batt_size)) else bank_length - (bank_length - end_batt_size) - 1

        # Run through the picks from the min to max pos
        for i, pos_val in enumerate(batt_picks[min_pos:max_pos + 1]):

            # Battery is picked
            if battery > pos_val:

                batt_picks[i + min_pos] = battery

                # now blank all following selections so they end up re-written
                for x in range(i + min_pos + 1, end_batt_size):
                    batt_picks[x] = 0
                break

    total_joltage += int("".join(str(x) for x in batt_picks))

print(f'Total joltage: {total_joltage}')