import re

total_worth = 0

with open('input-04.txt') as input:
    for line in input:
        lists = re.split(':|\|', line.strip())
        print(lists)

        winning_numbers = [int(number) for number in lists[1].strip().split(' ') if number]
        my_numbers = [int(number) for number in lists[2].strip().split(' ') if number]

        print(f'{winning_numbers}, {my_numbers}')

        won_numbers = [nbr for nbr in my_numbers if nbr in winning_numbers]
        print(f'won = {won_numbers}')
        total_worth += 2 ** (len(won_numbers) - 1) if len(won_numbers) > 0 else 0

print(total_worth)
