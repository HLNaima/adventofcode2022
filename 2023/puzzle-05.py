nbr_overlaps = 0

with open('test-05.txt') as input:
    lines = input.readlines()
    matrix = [[] for i in range(len(lines[0].strip()))]

    for idx, line in enumerate(lines):
        print(line)
        if line[1] == '1':
            break;
        else:
            for i in range(1, len(line), 4):
                if line[i] != ' ':
                    matrix[i//4].insert(0, line[i])

    print(matrix)
    
    for line in lines[idx + 1:]:
        move = line.stript().split(' ')
        quantity = move[1]
        from_stack = move[3]
        to_stack = move[5]

        for _ in range(quantity):
            crate = matrix[from_stack -1].pop()
            matrix[to_stack - 1].append()
