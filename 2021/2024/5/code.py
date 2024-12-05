import re
import sys
from functools import reduce
from collections import Counter
import math




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
            
            input_data = file.read().split("\n\n")
            rules = sorted(input_data[0].split("\n"))
            lines = input_data[1].split("\n")
            #print(rules)
         
            # is the row i the right order
            # find the middle page
            # are both numbers in list
            # is the number x before number y

            ## build a list of numbers that  must be before

            d = dict()
            total = list()

            for r in rules:
                split_for_map = r.split("|")
                x = int(split_for_map[1])
                y = int(split_for_map[0])

                if x in d:
                    d[x].append(y)
                else:
                    d[x] = list()
                    d[x].append(y)
                    d[x] = sorted(d[x])


            

            for ln in lines:
                nums = [int(n) for n in ln.split(",")]
                safe = True

                ## this will check right to left
                next_nums_cant_be = list()
                
                
                for n in nums:
                    print(n)

                # half = int((len(nums) - 1) / 2)

                # if safe is True:
                #     #print(total)
                #     total.append(nums[half])
                #     print(sum(total))


    def puzzle_two(self):
        
        with open(self.file,"r") as file:
            
            input_data = file.read().split("\n\n")
            rules = sorted(input_data[0].split("\n"))
            lines = input_data[1].split("\n")
            #print(rules)
                
#day().puzzle_one()
day().puzzle_two()
