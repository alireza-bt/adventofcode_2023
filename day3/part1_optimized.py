"""
any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)
What is the sum of all of the part numbers in the engine schematic?
"""

import re
from collections import defaultdict

# Open the file containing engine parts information
with open("day3/engine_parts.txt", 'r') as f:
    # Read lines from the file and split them
    lines = f.read().splitlines()
    
    ans = 0  # Initialize the sum of numeric values

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

            # Count the number of adjacent symbols to the current numeric value
            count = sum(
                0 <= row < len(lines) and 0 <= col < len(lines[row]) and
                lines[row][col] != '.' and not lines[row][col].isdigit()
                for row, col in idx
            )

            # If there are adjacent symbols, add the numeric value to the sum
            if count > 0:
                ans += int(m.group())

    # Print the final result
    print(ans)