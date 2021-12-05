import numpy as np
from functools import reduce

def print_card(card):
    for line in card:
        print(line)


def merge_lists(list_of_lists):
    return reduce(lambda x,y: x+y, list_of_lists)

def make_some_cards(data):
    data = [int(x) for x in data if x] 
    return [data[x:x+25] for x in range(0, len(data),25)]

def dobber(call, card):
    return [-1 if x == int(call) else x for x in card]

def check_row(card):
    rows = [card[x:x+5] for x in range(0, len(card),5)]

    #print(rows)

    for r in rows:
        if sum(r) == -5:
            return rows
        else:
            return False



def count_points(winning_card, last_call):
    flat_list = merge_lists(winning_card)
    no_dobbed = [x for x in merge_lists(winning_card) if x > -1]
    return sum(no_dobbed) * 24


def check_col(card):
    columns = []

    for c in range(0,25,5):
        columns.append(card[c + 0])
        columns.append(card[c + 1])
        columns.append(card[c + 2])
        columns.append(card[c + 3])
        columns.append(card[c + 4])

    return check_row(columns)

def test_main():
    data = open('data.txt').read().strip("\n\n").split()
    calls = data[0].split()[0].split(",")
    data.pop(0)
    card_data = make_some_cards(data) 
    card = card_data[0]

    

    

    for index, call in enumerate(calls):
        card = dobber(call, card)
        rows = check_row(card)
        col = check_col(card)

        if rows:
            print("This winner is...")
            print_card(rows)
            print("With a score of...")
            print(count_points(rows, int(call)))
            break


        if col: 
            print("This winner is...")
            print_card(col)
            print("With a score of...")
            print(count_points(col, int(call)))
            break       

    return [calls, make_some_cards(data)]
    return

test_main()



#cards =  make_some_cards(all_numbers)


# winner = play_the_game()
# print(count_points(winner))
