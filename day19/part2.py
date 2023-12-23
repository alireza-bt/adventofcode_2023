"""
"""
import re
from collections import defaultdict
from functools import cache
import sys
from copy import deepcopy

#sys.setrecursionlimit(1000)

ans = 0

lines = []

def end_sum(xmas):
    m = 1
    for s, e in xmas.values():
        m *= (e-s+1)
    return m

def recursive_range_run(xmas, rule):
    rangesum = 0
    print(rule)
    if ',' in rules[rule]:
        flow = rules[rule].split(',')
    else:
        flow = [rules[rule]]
    for r in flow:
        if ':' in r:
            con, to = r.split(':')
            if '>' in con:
                val, num = con.split('>')
                newXmas = deepcopy(xmas)
                if newXmas[val][0] > int(num):
                    newXmas[val][0] = max(xmas[val][0], int(num)+1)
                    if to == 'A':
                        rangesum += end_sum(newXmas)
                    elif to != 'R':
                        rangesum += recursive_range_run(newXmas, to)
                    xmas[val][1] = min(xmas[val][1], int(num))
            
            if '<' in con:
                val, num = con.split('<')
                newXmas = deepcopy(xmas)
                if newXmas[val][0] < int(num):
                    newXmas[val][1] = min(xmas[val][1], int(num)-1)
                    if to == 'A':
                        rangesum += end_sum(newXmas)
                    elif to != 'R':
                        rangesum += recursive_range_run(newXmas, to)
                    xmas[val][0] = max(xmas[val][0], int(num))
            
        else:
            if r == 'A':
                rangesum += end_sum(xmas)
            elif r != 'R':
                rangesum += recursive_range_run(xmas, r)
    return rangesum


with open('day19/input.txt', 'r') as f:
    # Read input until first empty line
    rules = {}
    while True:
        line = f.readline().strip()
        if line == '':
            break
        name, rule = line.split('{')
        rules[name] = rule[:-1] # Remove closing '}'


print("Print for part 2 the answer is: ", 
      recursive_range_run({"x": [1, 4000], "m": [1, 4000], "a": [1, 4000], "s": [1, 4000]}, "in"))



# print(ans)
