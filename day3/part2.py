
import re

# List to store positions of symbols in the form of "row,column"
symbol_positions = []
line_length = 0  # Length of each line in the input file
row_count = 0    # Number of rows in the input file

def index_is_valid(i, c):
    """Check if the given row index 'i' and column index 'c' are within valid bounds."""
    return 0 <= i < row_count and 0 <= c < line_length

def has_adjacent_symbol(tuple, row):
    """Check if there is at least one adjacent symbol to the specified position."""
    for i in range(row - 1, row + 2):  # Iterate over rows (i-1, i, i+1)
        for c in range(tuple[1] - 1, tuple[2] + 1):  # Iterate over columns (start-1, stop)
            if index_is_valid(i, c) and f"{i},{c}" in symbol_positions:
                return True
    return False

# Open the file containing engine parts information
with open("day3/engine_parts.txt", 'r') as f:
    sum_of_adjacents = 0
    i = 0
    for l in f:
        if i == 0:
            line_length = len(l)
        # Extract symbol positions from each line and add them to the list
        symb_pos_line = [f"{i},{m.start(0)}" for m in re.finditer(r'[^\d\.\n]', l)]
        symbol_positions += symb_pos_line
        i += 1
    row_count = i

# Open the file again to calculate the sum of values adjacent to symbols
with open("day3/engine_parts.txt", 'r') as f:
    sum_of_adjacents = 0
    i = 0
    for l in f:
        # Extract numeric values and their positions from each line
        numbers = [(m.group(), m.start(0), m.end(0)) for m in re.finditer(r'\d+', l)]
        for n in numbers:
            # Add the numeric value to the sum if it has an adjacent symbol
            sum_of_adjacents += int(n[0]) if has_adjacent_symbol(n, i) else 0
        i += 1
    print("Sum of values adjacent to symbols: %d" % sum_of_adjacents)