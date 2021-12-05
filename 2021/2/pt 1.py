from typing import ForwardRef


data = open('data.txt').read().split("\n")

forward = 0
down = 0 


aim = 0
horiz = 0
depth = 0

testdata = ["forward 5","down 5","forward 8","up 3","down 8","forward 2"]

for pos in data:
    #print(pos)
    possie = pos.split()
    print(pos)
    
    if possie[0] == "up":
        #down = down - int(possie[1])
        aim = aim - int(possie[1])

    if possie[0] == "down":
        #down = down + int(possie[1])
        aim = aim + int(possie[1])

    if possie[0] == "forward":
        horiz = horiz + int(possie[1])
        depth = depth + aim * int(possie[1])
        
        print(horiz , depth, aim)

#print(forward *down)
print(horiz , depth, aim)
print(horiz * depth)