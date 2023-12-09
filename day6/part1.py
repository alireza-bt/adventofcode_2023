"""
for solving part 2 I needed to change the input file instead and remove the spaces
"""
import re
from collections import defaultdict
from numpy import polynomial as poly
import math

ans = 1
#ans = 0

with open("day6/races.txt", 'r') as f:
    lines = f.read().splitlines()

times = [int(i) for i in re.findall(r'\d+', lines[0])]
dists = [int(i) for i in re.findall(r'\d+', lines[1])]

for t, d in zip(times, dists):
    roots = poly.polynomial.Polynomial(coef=[-1*d,t,-1]).roots()
    if len(roots) == 2:
       count = math.ceil(roots[1])-1 - (math.floor(roots[0])+1) + 1
    #print(roots)
    
    ans *= count
print(ans)
"""TODO: change the search direction"""