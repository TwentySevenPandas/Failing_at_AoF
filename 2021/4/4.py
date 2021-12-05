calls = [57,9,8,30,40,62,24,70,54,73,12,3,71,95,58,88,23,81,53,80,22,45,98,37,18,72,14,20,66,0,19,31,82,34,55,29,27,96,48,28,87,83,36,26,63,21,5,46,33,86,32,56,6,38,52,16,41,74,99,77,13,35,65,4,78,91,90,43,1,2,64,60,94,85,61,84,42,76,68,10,49,89,11,17,79,69,39,50,25,51,47,93,44,92,59,75,7,97,67,15]
tst = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

from functools import reduce

def check_results(card):
    start = 0

    hozzie = 0
    row = 0
    while row < 6:
        for hoz_num in range(5): # move accross row
            hozzie += card[hoz_num]
        
        if(hozzie == -5):
            return True
        else:
            row += 1
        
    vertie = 0
    col = 0
    while row < 6:
        for vert_num in range(5): # move accross row
            vertie += card[vert_num]
        
        if(vertie == -5):
            return True
        else:
            col += 5

    return False

def make_some_cards(data):
    data = [int(item) for item in data]
    return [data[x:x+25] for x in range(0, len(data),25)]
     

def dobber(call, card):
    return [-1 if x == int(call) else x for x in card]


def play_the_game():
    for call in calls:
        for index, card in enumerate(cards):
            cards[index] = dobber(int(call), cards[index])
            if check_results(cards[index]) == True:
               return [cards[index], call]


def count_points(winning_card):
    print(winning_card)
    no_dobbed = [x for x in winning_card[0] if x > -1]
    return sum(no_dobbed) * winning_card[1]



all_numbers = open('data.txt').read().strip("\n").split()

cards =  make_some_cards(all_numbers)

winner = play_the_game()
#print(winner)
print(count_points(winner))
