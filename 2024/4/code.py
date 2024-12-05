import re
import sys
from functools import reduce
from collections import Counter




# A Sample class with init method
class day:

    # init method or constructor
    def __init__(self):
        self.file = sys.argv[1]
        with open(self.file,"r") as file:
            self.file_as_lines =  file.read().splitlines() 

        self.numbers = "0123456789"
        self.regex_symols = '[^\\d\\.]' #carrot means not equal to    
        self.regex_numbers = '\\d+'
        

               
    def puzzle_one(self):
        
        with open(self.file,"r") as file:
            
            input_data = file.read().strip().split("\n")
            count = 0
            for ln_i, ln in enumerate(input_data):
                xmas_ln = re.findall("XMAS",ln)
                samx_ln = re.findall("SAMX",ln)
                count += (len(xmas_ln) + len(samx_ln))


            for col_i, col in enumerate(input_data[0])
                col_val = ""
                for c_i, c in input_data[0]:
                    col_val += col_i
                                            
            
            print(count)
                         
                        



       

day().puzzle_one()

# res, valid = [0, 0], 1
# with open("data.txt") as file:
#     line = file.read()
#     for match in re.findall(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))", line):
#         print(match)
#         if match[0]:
#             valid = 1
#         elif match[1]:
#             valid = 0
#         else:
#             x = int(match[3]) * int(match[4])
#             res[0] += x
#             res[1] += x * valid
# print(res)     