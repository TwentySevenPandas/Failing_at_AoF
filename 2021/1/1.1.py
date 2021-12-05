
data = open('data.txt').read().split("\n")
seq = [0, 1, 2, 3, 4, 5]
window_size = 3

total = 0
pos = 0
last = 0


for i in range(len(data) - window_size + 1):
    win = data[i: i + window_size] #make my windows
    winTotal = sum([int(item) for item in win]) #sum as int

    if pos > 0 and winTotal > int(last):
       total +=1

    last = winTotal
    pos  += 1


print(total)








# total = -1
# last = 0
# window_a = [0,0,0]
# window_b = [0,0,0]


# count = 0
# for line in open('data1.txt').xreadlines(  ): count += 1


# with open('data1.txt') as topo_file:
#     for index, line in enumerate(topo_file):
        

#         #print(line, last)
#         if int(line) > int(last):
#             total = total + 1
            
#         last = line
        

# print(total)          




#         # dimArray = line.split("x")
#         # l = int(dimArray[0])
#         # w = int(dimArray[1])
#         # h = int(dimArray[2])
#         # total = total + boxSize(l, w, h)  # The comma to suppress the extra new line char`
