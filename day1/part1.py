"""The newly-improved calibration document consists of lines of text; 
each line originally contained a specific calibration value that the Elves now need to recover. 
On each line, the calibration value can be found by combining the first digit 
and the last digit (in that order) to form a single two-digit number.
"""
import re

with open('cal_doc.txt', 'r') as f:
    calibration_val = 0
    for l in f:
        all_matches = []
        all_matches = re.findall(r"\d", l)
        if len(all_matches) >= 1:
            calibration_val += int(all_matches[0]+all_matches[-1])
        else:
            print('no digit in line')
    print("calibration value: %d" % calibration_val)