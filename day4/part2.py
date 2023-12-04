"""
"""

import re
from collections import defaultdict

star_dict = defaultdict(int)
ans = 0

with open("day4/card_list.txt", 'r') as f:
    for id, l in enumerate(f):
        # id = int(re.search(r"\d+", l.split(': ')[0]).group(0)) # numbers
        _, line = l.split(': ')
        win_list, num_list = map(str.split, line.split(" | "))
        # print (win_list)
        # print (num_list)
        star_dict[id] += 1
        cnt = sum(num_list.count(n) for n in win_list)
        #print(cnt)
        for i in range(1, cnt+1):
            star_dict[id+i] += star_dict[id]
        # print(cnt)
        #ans += pow(2, cnt-1) if cnt > 0 else 0
        #ans += 1 #?
print(sum(star_dict.values()))
