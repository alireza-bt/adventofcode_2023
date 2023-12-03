"""
any number adjacent to a symbol, even diagonally, is a "part number" and should be included in your sum. 
(Periods (.) do not count as a symbol.)
What is the sum of all of the part numbers in the engine schematic?
"""

import re
from collections import defaultdict

with open("day3/engine_parts.txt", 'r') as f:
    lines = f.read().splitlines()
    ans = 0
    for i, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            idx = [(i, m.start()-1), (i, m.end())]
            idx += [(i-1, j) for j in range(m.start()-1, m.end()+1)]
            idx += [(i+1, j) for j in range(m.start()-1, m.end()+1)]
            # find the adjacents symbols to each number
            count = sum(0 <= row < len(lines) and 0 <= col < len(lines[row]) and lines[row][col] != '.' and not lines[row][col].isdigit() for row, col in idx) 
            if count > 0:
                ans += int(m.group())
    print(ans)
