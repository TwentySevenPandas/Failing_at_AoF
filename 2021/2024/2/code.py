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

        with open(self.file, 'r') as file:
            reports = []
            for line in file:
                reports.append(list(map(int, line.split())))

        def is_safe(report):
            if report == sorted(report) or report == sorted(report, reverse=True):
                for i in range(len(report) - 1):
                    if abs(report[i] - report[i + 1]) <= 0 or abs(report[i] - report[i + 1]) >= 4:
                        return False
                return True
            return False

        one = 0
        two = 0

        for report in reports:
            if is_safe(report):
                one += 1
                two += 1
            else:
                for i in range(len(report)):
                    new_report = report[:i] + report[i + 1:]
                    if is_safe(new_report):
                        two += 1
                        break

        print(one)
        print(two)


day().puzzle()