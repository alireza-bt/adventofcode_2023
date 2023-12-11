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
    path.append(f"{r},{c}")
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
    lines = f.read().splitlines()
    start = []
    
    r_max = len(lines)-1
    c_max = len(lines[0])-1

    for idx, l in enumerate(lines):
        if 'S' in l:
            start = [idx, l.find('S')]
            break

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
pos, next = move(start, 1)
while next > -1:
    pos, next = move(pos, next)


print(math.ceil((ans-1)/2))
#print(path)
