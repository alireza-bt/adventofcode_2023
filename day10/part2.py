"""
"""
import re
from collections import defaultdict
import math

r_max = 0
c_max = 0
lines = []
ans = 0
path = []

map = defaultdict(list)

def has_indirect_neighbour(r, c):
    pass

def mark_cell(r, c):
    if lines[r][c] == 'X' or lines[r][c] == '0':
        return None
    
    # check direct neighbours
    if c < c_max and lines[r][c+1] == '0':
        lines[r][c] = '0'
    if c > 0 and lines[r][c-1] == '0':
        lines[r][c] = '0'
    if r < r_max and lines[r+1][c] == '0':
        lines[r][c] = '0'
    if r > 0 and lines[r-1][c] == '0':
        lines[r][c] = '0'

    #check indirect neighbours
    #has_indirect_neighbour(r,c)




def next_move(shape, last_move):
    match shape:
        case '|':
            return last_move
        case '-':
            return last_move
        case 'J':
            return 0 if last_move == 1 else 3
        case '7':
            return 2 if last_move == 1 else 3
        case 'L':
            return 1 if last_move == 2 else 0
        case 'F': 
            return 1 if last_move == 0 else 2
        case _:
            return -1

def move(pos, next):
    r, c = pos
    global ans, path
    ans += 1
    path.append((r, c))
    # first move then analyze again
    match next:
        case -1:
            return None
        case 0: # means I will be in pos-1, pos
            return [r-1, c], next_move(lines[r-1][c], next)
        case 1: # means I will be in pos-1, pos
            return [r, c+1], next_move(lines[r][c+1], next)
        case 2: # means I will be in pos-1, pos
            return [r+1, c], next_move(lines[r+1][c], next)
        case 3: # means I will be in pos-1, pos
            return [r, c-1], next_move(lines[r][c-1], next)


with open("day10/pipes.txt", 'r') as f:
    lines = []
    for l in f.read().splitlines():
        lines.append(list(l))
    start = []
    
    r_max = len(lines)-1
    c_max = len(lines[0])-1

    for idx, l in enumerate(lines):
        if 'S' in l:
            start = [idx, l.index('S')]
            break

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
pos, next = move(start, 1)
while next > -1:
    pos, next = move(pos, next)

for i in path:
    (x, y) = i
    lines[x][y] = 'X'


# replace the first row
for c in range(c_max):
    if lines[0][c] != 'X':
        lines[0][c] = '0'
        if lines[1][c] != 'X': # direct neighbour
            lines[1][c] = '0'
    if lines[-1][c] != 'X':
        lines[-1][c] = '0'
        if lines[-2][c] != 'X': # direct neighbour
            lines[-2][c] = '0'
for i in range(r_max):
    if lines[i][0] != 'X':
        lines[i][0] = '0'
        if lines[i][1] != 'X': # direct neighbour
            lines[i][1] = '0'
    if lines[i][-1] != 'X':
        lines[i][-1] = '0'
        if lines[i][-2] != 'X': # direct neighbour
            lines[i][-2] = '0'

i, j = 1, 1
while i <= r_max/2:
    for c in range(c_max):
        mark_cell(i, c)
        mark_cell(-1-i, c)

    for r in range(r_max):
        mark_cell(r, j)
        mark_cell(r, -1-j)

    i += 1
    j += 1

# print(math.ceil((ans-1)/2))
#print(path)

with open('test.txt', 'w') as f:
    for line in lines:
        f.write(''.join(line))
        f.write('\n')
