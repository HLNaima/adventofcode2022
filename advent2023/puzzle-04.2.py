import re

def nbr_wins(winning_numbers_str, my_numbers_str):
    winning_numbers = [int(number) for number in winning_numbers_str.strip().split(' ') if number]
    my_numbers = [int(number) for number in my_numbers_str.strip().split(' ') if number]

    won_numbers = [nbr for nbr in my_numbers if nbr in winning_numbers]
    
    return len(won_numbers)


scratches_nbr = 0

cards_count = {}

with open('input-04.txt') as input:
    for line in input:
        lists = re.split(':|\|', line.strip())
        print(lists)

        card_number = int(lists[0].split(' ')[-1])
        card_wins_nbr = nbr_wins(lists[1], lists[2])

        print(card_number)
        print(card_wins_nbr)

        if card_number in cards_count:
            cards_count[card_number] += 1
        else:
            cards_count[card_number] = 1

        for i in range(1, card_wins_nbr + 1):
            if card_number + i in cards_count:
                cards_count[card_number + i] += cards_count[card_number]
            else:
                cards_count[card_number + i] = cards_count[card_number]
        print(cards_count)
        scratches_nbr += cards_count[card_number]
print(cards_count)
print(scratches_nbr)

