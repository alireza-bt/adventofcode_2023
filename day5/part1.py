"""
"""
import re
from collections import defaultdict

ans = defaultdict(int)
#ans = 0

with open("day5/map.txt", 'r') as f:
    map_name = ''
    for l in f.read().splitlines():
        if 'seeds:' in l:
            seeds = re.findall(r'\d+', l)
            for s in seeds:
                ans[int(s)] = int(s) #each seed maps to itself, except when we get another map for them
        elif 'map:' in l:
            #print(ans)
            new_dict = defaultdict(int)
            for i in ans.values():
                new_dict[i] = i
            ans = new_dict # for new map we have the sources now (destinations of the last map)

        elif len(l) > 0 and l[0].isdigit(): # start of map
            dest_start, src_start, r = l.split(' ')
            #print(f"{src_start, dest_start}")
            keys = list(ans.keys())
            for k in keys:
                if int(src_start) <= k <= int(src_start)+int(r):
                    ans[k] = int(dest_start) + k - int(src_start)
            
        # _, line = l.split(': ')
        # win_list, num_list = map(str.split, line.split(" | "))
        # # print (win_list)
        # # print (num_list)
        # cnt = sum(num_list.count(n) for n in win_list)
        # # print(cnt)
        # ans += pow(2, cnt-1) if cnt > 0 else 0
print(min(ans.values()))

"""TODO: change the search direction"""