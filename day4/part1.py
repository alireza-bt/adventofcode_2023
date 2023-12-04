"""
"""

ans = 0
with open("day4/card_list.txt", 'r') as f:
    for l in f.read().splitlines():
        _, line = l.split(': ')
        win_list, num_list = map(str.split, line.split(" | "))
        # print (win_list)
        # print (num_list)
        cnt = sum(num_list.count(n) for n in win_list)
        # print(cnt)
        ans += pow(2, cnt-1) if cnt > 0 else 0
print(ans)
