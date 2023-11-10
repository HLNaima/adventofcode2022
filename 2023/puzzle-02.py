with open('input-02.txt') as input:
    total_score = 0
    for line in input:
        p, m = line.strip().split(' ')
        p, m = ord(p) - 64, ord(m) - 87
        
        total_score += m + ((1 + m - p) % 3) * 3

print(f"Total score = {total_score}")
