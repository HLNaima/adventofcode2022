with open('input-02.txt') as input:
    total_score = 0
    for line in input:
        p, m = line.strip().split(' ')
        p, m = ord(p) - 64, ord(m) - 87
        
        total_score += m + ((1 + m - p) % 3) * 3
    print(f"Total score when second entry is what should be played = {total_score}")

with open('input-02.txt') as input:
    total_score = 0
    for line in input:
        p, s = line.strip().split(' ')
        p, s = ord(p) - 64, ord(s) - 88
        
        total_score += ((1 + p + s) % 3) + 1 + s * 3
    print(f"Total score when second entry is the outcome of the round = {total_score}")
