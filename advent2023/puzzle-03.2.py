res = 0

def is_digit(char):
    return ord(char) >= 48 and ord(char) <= 57

def get_number(line, pos):
    i = pos
    number = ""
    while i < len(line) and is_digit(line[i]):
        number += line[i]
        i += 1
    
    i = pos - 1
    while i >= 0 and is_digit(line[i]):
        number = line[i] + number
        i -= 1
    
    return (int(number), i + 1)

def get_gear_ratio(line, previous_l, next_l, pos):
    numbers = []
    prev_starts = []
    next_starts = []
    for i in range(pos - 1 if pos > 0 else 0, pos + 2 if pos < len(line) - 2 else len(line)):
        if is_digit(line[i]):
            number, _ = get_number(line, i)
            numbers.append(number)
        if previous_l and is_digit(previous_l[i]):
            number, prev_start = get_number(previous_l, i)
            if prev_start not in prev_starts:
                numbers.append(number)
                prev_starts.append(prev_start)
        if next_l and is_digit(next_l[i]):
            number, next_start = get_number(next_l, i)
            if next_start not in next_starts:
                numbers.append(number)
                next_starts.append(next_start)

    print(numbers)

    return numbers[0] * numbers[1] if len(numbers) == 2 else 0

with open('input-03.txt') as input:
    lines = [line.strip() for line in input]
    for idx, line in  enumerate(lines):
        previous_l = lines[idx - 1] if idx > 0 else []
        next_l = lines[idx + 1] if idx < len(lines) - 1 else []

        for i in range(len(line)):
            if line[i] == '*':
                print(line)
                res += get_gear_ratio(line, previous_l, next_l, i)
print(res)
