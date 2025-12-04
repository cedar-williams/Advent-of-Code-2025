# --- Day 3: Lobby ---

# Import battery banks
with open("input.txt") as file:
    banks = [line.strip() for line in file]

# Find max joltage for each bank
total_joltage = 0

for bank in banks:
    l_batt = 0 # Left battery
    r_batt = 0 # Right battery

    bank_length = len(bank)
    for index, battery in enumerate(map(int, bank)):

        # If battery larger than l (10's place) and not last in bank
        if (battery > l_batt) and (index < bank_length - 1):
            l_batt = battery
            r_batt = 0 # Set back to 0 so it's reassigned on the next iteration

        # If battery is last in bank and larger than r_batt, always true if r_batt is 0
        elif (index == bank_length - 1) and (battery > r_batt):
            r_batt = battery

        # If battery is larger than r_batt
        elif (battery > r_batt):
            r_batt = battery

    total_joltage += int(str(l_batt) + str(r_batt))

print(f'Total joltage: {total_joltage}')