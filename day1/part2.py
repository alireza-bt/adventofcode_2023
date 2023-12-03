"""--- Part Two ---

Your calculation isn't quite right. It looks like some of the digits are actually spelled out with letters: one, two, three, four, five, six, seven, eight, and nine also count as valid "digits".

Equipped with this new information, you now need to find the real first and last digit on each line. For example:
"""
import re
string_lst = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def digit_value(x):
    if(x.isdigit()):
        return x
    else:
        return str(string_lst.index(x)+1)
with open('cal_doc.txt', 'r') as f:
    calibration_val = 0
    for l in f:
        all_matches = []
        #all_matches = re.findall(r"\d", l)
        all_matches = re.findall(r"(?=("+'|'.join(string_lst)+'|\d'+r"))", l)
        if len(all_matches) >= 1:
            #print(digit_value(all_matches[0]) + digit_value(all_matches[-1]))
            calibration_val += int(digit_value(all_matches[0]) + digit_value(all_matches[-1]))
        else:
            print('no digit in line')
    print("calibration value: %d" % calibration_val)