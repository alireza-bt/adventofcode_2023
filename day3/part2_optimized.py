"""
A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.
What is the sum of all of the gear ratios in your engine schematic?

"""

import re
from collections import defaultdict

# Open the file containing engine parts information
with open("day3/engine_parts.txt", 'r') as f:
    # Read lines from the file and split them
    lines = f.read().splitlines()

    ans = 0  # Initialize the final result
    adj = defaultdict(list)  # Default dictionary to store adjacent numeric values for each symbol

    # Iterate over each line in the grid
    for i, line in enumerate(lines):
        # Iterate over numeric values found in the line using regex
        for m in re.finditer(r'\d+', line):
            # Create a list of positions surrounding the current numeric value
            idx = [
                (i, m.start()-1),
                (i, m.end()),
                *[(i-1, j) for j in range(m.start()-1, m.end()+1)],
                *[(i+1, j) for j in range(m.start()-1, m.end()+1)]
            ]

            # Find adjacent symbols to each numeric value and store them in the defaultdict
            for row, col in idx:
                if 0 <= row < len(lines) and 0 <= col < len(lines[row]) and lines[row][col] != '.' and not lines[row][col].isdigit():
                    adj[row, col].append(int(m.group()))

    # Calculate the final result by summing the product of pairs of numeric values for each symbol
    ans = sum(a[0] * a[1] for a in adj.values() if len(a) == 2)

    # Print the final result
    print(ans)
