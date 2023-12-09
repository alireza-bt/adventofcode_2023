"""
"""
import re
from collections import defaultdict
from numpy import polynomial as poly
import math

map = defaultdict(list)

with open("day8/map.txt", 'r') as f:
    lines = f.read().splitlines()
    # instruction = [0 if i == 'L' else 1 for i in lines[0]]
    instruction = ["LR".find(i) for i in lines[0]] #easier way to assign 0, 1 instead of L, R

    for l in lines[2:]:
        # k, v = l.split(' = ')
        # map[k] = [i for i in re.findall(r'[A-Z]+', v)]
        k, y, z = re.findall(r'\w+', l)
        map[k] = [y, z]

position = 'AAA'
counter = 0
while position != 'ZZZ':
    # if counter == len(instruction):
    #     counter = 0
    position = map[position][instruction[counter%len(instruction)]]
    counter += 1

print(counter)
