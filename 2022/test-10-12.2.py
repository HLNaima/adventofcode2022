def print_crt():
    for line in crt:
        print("".join(line))


def next_cycle():
    global cycles, line

    crt_position = cycles % 40
    if crt_position in range(register - 1, register + 2):
        crt[line].append('#')
    else:
        crt[line].append('.')

    cycles += 1
    if cycles % 40 == 0:
        line += 1
        crt.append([])


with open("input-10-12.txt", "r") as input_data_file:
    raw_instructions = input_data_file.readlines()

cycles = 0
register = 1

crt = [[]]
line = 0
for instruction in raw_instructions:
    instruction = instruction.strip().split(' ')
    operation = instruction[0]
    if operation == 'addx':
        operand = int(instruction[1])
        next_cycle()
        next_cycle()
        register += operand
    else:
        next_cycle()
print_crt()
