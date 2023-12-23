"""
"""
import re
from collections import defaultdict
from functools import cache
import sys
import copy

#sys.setrecursionlimit(1000)

ans = 0

lines = []

with open('day19/input.txt', 'r') as f:
    # Read input until first empty line
    rules = {}
    while True:
        line = f.readline().strip()
        if line == '':
            break
        name, rule = line.split('{')
        rules[name] = rule[:-1] # Remove closing '}'
    
    # continue reading input until EOF
    ratings = {}
    idx = 0
    while True:
        line = f.readline().strip()
        if not line:
            break
        dict = {}
        for i in line[1:-1].split(','):
            
            attr, val = i.split('=')
            dict[attr] = int(val)
        ratings[idx] = dict
        idx += 1

for i in range(len(ratings)):
    print(i)
    f = 'in'
    done = False
    while not done:
        print(done)
        if f == 'A':
            done = True
            ans += sum(ratings[i].values())
            break
        if f == 'R':
            done = True
            break
        for r in rules[f].split(','):
            if r == 'A':
                done = True
                ans += sum(ratings[i].values()) # sum of all the values in rating
                break
            if r == 'R':
                done = True
                break

            if ':' in r:
                op, goto = r.split(':')
                if '<' in op:
                    if ratings[i][op[0]] < int(op[2:]):
                        f = goto
                        break
                elif '>' in op:
                    if ratings[i][op[0]] > int(op[2:]):
                        f = goto
                        break
            else:
                f = r
                break

print(ans)
