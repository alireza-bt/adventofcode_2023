"""

"""

import re

symbol_positions = []
line_length = 0
row_count = 0

def index_is_valid(i, c):
    if i >= 0 and i < row_count and c >= 0 and c < line_length:
        return True
def has_adjecent_symbol(tuple, row):
    #print(tuple)
    for i in range(row-1, row+2): # i-1, i, i+1
        for c in range(tuple[1]-1, tuple[2]+1): # start-1 ... stop
            #print(str(i)+','+str(c))
            if index_is_valid(i, c) and str(i)+','+str(c) in symbol_positions:
                #print("yes")
                return True
    #print("no")
    return False

with open("day3/engine_parts.txt", 'r') as f:
    sum_of_adjecents = 0
    i = 0
    for l in f:
        if i == 0:
            line_length = len(l)
        # we don't need the symbols but only their position:
        symb_pos_line = [str(i)+','+str(m.start(0)) for m in re.finditer(r'[^\d\.\n]', l)]
        symbol_positions += symb_pos_line
        i+=1
    row_count = i
    # print("Sum of valid game IDs: %d" % sum_of_valids)
    #print(symbol_positions)

with open("day3/engine_parts.txt", 'r') as f:
    sum_of_adjecents = 0
    i = 0
    for l in f:
        numbers = [(m.group(), m.start(0), m.end(0)) for m in re.finditer(r'\d+', l)]
        for n in numbers:
            sum_of_adjecents += int(n[0]) if has_adjecent_symbol(n, i) else 0
        i+=1
    print("sum of adjacents to symbs: %d"%sum_of_adjecents)
