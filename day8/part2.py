"""
"""
import re
from collections import defaultdict

map = defaultdict(list)

with open("day8/map.txt", 'r') as f:
    lines = f.read().splitlines()
    #instruction = [0 if i == 'L' else 1 for i in lines[0]]
    instruction = ["LR".find(i) for i in lines[0]] #easier way to assign 0, 1 instead of L, R

    for l in lines[2:]:
        # k, v = l.split(' = ')
        # map[k] = [i for i in re.findall(r'\w+', v)]
        k, y, z = re.findall(r'\w+', l)
        map[k] = [y, z]

positions = [i for i, _ in map.items() if i[2]=='A']
#position = 'AAA'
times = []
for p in positions:
    counter = 0
    position = p
    # if counter == len(instruction):
    #     counter = 0
    while position[2] != 'Z':
        position = map[position][instruction[counter%len(instruction)]] 
        counter += 1
    times.append(counter)
print(times)
from math import lcm
print(lcm(*times))
