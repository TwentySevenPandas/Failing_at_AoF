

# 4273224
from collections import Counter

# takea all the elements at the pos postion and puts them in a list
def get_nums(data, pos):
    store = []
    for bin in data:
        store.append(bin[pos])
    
    return store

data = open('data copy.txt').read().split("\n")
clean_data = [x for x in data if x]


# what is a turple
# what is position -1 in a list

##########################################################################
#
# Part One
#
########################################################################## 

# gamma = ""
# epsilon = ""
# pos = 0

# while pos < len(clean_data[0]):
#     hold = get_nums(clean_data, pos)
#     counts = Counter(hold).most_common() # returns turple - what is a turple
#     epsilon += list(counts[1])[0]# what is position -1 in a list
#     gamma += list(counts[0])[0]
#     pos +=1
#     # print(epsilon)
        
# print(int(gamma, 2) * int(epsilon, 2))


##########################################################################
#
# Part Two
#
##########################################################################

def removeCharAt(charry, pos, thing):
    return 1 if int(charry[pos]) == thing else 0

def getMost(c):
    return 1 if c[1][1] == c[0][1] else int(c[0][0])

def getLeast(c):
    return 0 if c[1][1] == c[0][1] else int([1][0])

array = ['111110000000', '010110001111', '100110001111']
# print([x for x in array if removeCharAt(x,0,"1")])
#print(array[0])

pos = 0
otwo_gen = clean_data.copy()
cotwo_scrub = clean_data.copy()
loop_lenth = len(clean_data[0])

##print(otwo_gen)
while len(otwo_gen) > 1:
    
    allTheSingleNumbers = get_nums(clean_data, pos)
    counts = Counter(allTheSingleNumbers).most_common() # returns turple - what is a turple

    most = getMost(list(counts))
    
    otwo_gen = [x for x in otwo_gen if removeCharAt(x,pos,most)] 
    pos +=1


print()

least_pos = 0
while len(cotwo_scrub) > 1:
    
    allTheSingleNumbers2 = get_nums(clean_data, least_pos)
    counts = Counter(allTheSingleNumbers2).most_common() # returns turple - what is a turple

    least = getLeast(list(counts))

    cotwo_scrub = [x for x in cotwo_scrub if removeCharAt(x,least_pos,least)]  


    least_pos +=1
    
totoal = int(otwo_gen[0], 2) * int(cotwo_scrub[0],2)

print(int(otwo_gen[0], 2))
print(int(cotwo_scrub[0],2))




