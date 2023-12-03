res = 0

def contains_symbol(string):
    for char in string:
        if char != '.' and (ord(char) < 48 or ord(char) > 57):
            return True

def is_digit(char):
    return ord(char) >= 48 and ord(char) <= 57

def get_number(line, pos):
    i = pos
    number = ""
    while i < len(line) and is_digit(line[i]):
        number += line[i]
        i += 1
    
    return (number, len(number))

def is_part(line, prev_l, next_l, start, end):
    print(line[start:end])
    is_part = contains_symbol(line[start:end]) 
    if (prev_l):
        is_part = is_part or contains_symbol(prev_l[start:end])
        print(prev_l[start:end])
    
    if (next_l):
        is_part = is_part or contains_symbol(next_l[start:end])
        print(next_l[start:end])
    
    return is_part

with open('input-03.txt') as input:
    lines = [line.strip() for line in input]
    for idx, line in  enumerate(lines):
        print(line)
        previous_l = lines[idx - 1] if idx > 0 else []
        next_l = lines[idx + 1] if idx < len(lines) - 1 else []

        i = 0
        while i < len(line):
            char = line[i]
            if is_digit(char):
                number, size = get_number(line, i)
                if is_part(line, previous_l, next_l, i - 1 if i > 0 else 0, i + size + 1):
                    res += int(number)
                i += size
                print(f"{number} => {res}")
            else:
                i += 1
        
print(res)