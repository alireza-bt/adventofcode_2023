"""
"""
import re
from collections import defaultdict
from numpy import polynomial as poly
import numpy as np

ans = 0
gals = [] #list of r,c
double_rows = []
double_cols = []
with open("day11/map.txt", 'r') as f:
    lines = f.read().splitlines()
    for idx, l in enumerate(lines):
        cnt = 0
        for i in re.finditer(r'#', l):
            gals.append([idx, i.start()])
            cnt += 1
        if cnt == 0:
            double_rows.append(idx)

double_cols = [j for j in range(len(lines[0]))]
for g in gals:
    if g[1] in double_cols:
        double_cols.remove(g[1])

#renew gal positions
new_gals = []
for g in gals:
    #print(g[0])
    new_gals.append([g[0]+len([x for x in double_rows if x <= g[0]]*999999), g[1]+len([x for x in double_cols if x <= g[1]])*999999])

#print(new_gals)
#find paths
for i in range(len(new_gals)):
    for j in range(i+1, len(new_gals)):
        dist = abs(new_gals[i][0] - new_gals[j][0]) + abs(new_gals[i][1] - new_gals[j][1])
        ans+= dist
        #print(f"dist {i}, {j} -> {dist}")

print(ans)
