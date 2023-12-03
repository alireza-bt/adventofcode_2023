"""
A gear is any * symbol that is adjacent to exactly two part numbers. 
Its gear ratio is the result of multiplying those two numbers together.
What is the sum of all of the gear ratios in your engine schematic?

"""

import re
from collections import defaultdict

with open("day3/engine_parts.txt", 'r') as f:
    lines = f.read().splitlines()
    ans = 0
    adj = defaultdict(list)
    for i, line in enumerate(lines):
        for m in re.finditer(r'\d+', line):
            idx = [(i, m.start()-1), (i, m.end())]
            idx += [(i-1, j) for j in range(m.start()-1, m.end()+1)]
            idx += [(i+1, j) for j in range(m.start()-1, m.end()+1)]
            # find the adjacents symbols to each number
            for row, col in idx:
                if 0 <= row < len(lines) and 0 <= col < len(lines[row]) and lines[row][col] != '.' and not lines[row][col].isdigit():
                    adj[row, col].append(int(m.group()))
    ans = sum(a[0]*a[1] for a in adj.values() if len(a) == 2)
    print(ans)
