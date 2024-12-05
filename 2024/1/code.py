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
        
    #def check_in_range:
                
    def puzzle_one(self):
        
        with open(self.file,"r") as file:
            
            input_data = file.read().strip().split("\n")
            print(input_data)

            total = 0
            
            left = list()
            right = list()
            for nums in input_data:
                n = nums.split(" ")
                
                left.append(n[0])
                right.append(n[3])

            l = sorted(left)
            r = sorted(right)
            print(l)
            print(r)
            
            for c in range(0, len(l)):

                distance = int(r[c]) - int(l[c])


                if distance < 0:
                    distance = abs(distance)
                print(int(l[c]), int(r[c]),distance)
                total += distance

            print(total)
                
                
    def puzzle_two(self):
        
        with open(self.file,"r") as file:
            
            input_data = file.read().strip().split("\n")
            total = 0
            
            left = list()
            right = list()

            for nums in input_data:
                n = nums.split(" ")
                
                left.append(n[0])
                right.append(n[3])

            l = sorted(left)
            r = sorted(right)

            count_r = Counter(r)
            count_l = list(Counter(l))
            ##print(count)

            for l_num in l:
                x = int(l_num) * int(count_r[l_num])
                total += x
                print(total,x,l_num, int(count_r[l_num]))
        
 
            print("total",total) 

day().puzzle_one()
day().puzzle_two()