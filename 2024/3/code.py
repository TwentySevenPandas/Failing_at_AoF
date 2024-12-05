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
        

               

    def puzzle(self):
        
        

        results = [0, 0]
        is_valid = 1

        with open(self.file,"r") as file:
            file_content = file.read()
            valid_operations = []

            for match in re.findall(r"(do\(\))|(don't\(\))|(mul\((\d+),(\d+)\))", file_content):
                if match[0]:
                    is_valid = 1
                elif match[1]:
                    is_valid = 0
                    if len(valid_operations) > 0:
                        print("Number of valid operations:",len(valid_operations), "Operations:", valid_operations)
                    valid_operations = []
                else:
                    num1, num2 = int(match[3]), int(match[4])
                    total = num1 * num2
                    results[0] += total

                    if is_valid:
                        results[1] += total
                    if is_valid:
                        valid_operations.append((num1, num2))

        print(results)


day().puzzle()

