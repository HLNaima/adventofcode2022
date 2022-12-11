
with open("input-10-12.txt", "r") as input_data_file:
    raw_instructions = input_data_file.readlines()

cycles = 0
register = 1

signals = []

for instruction in raw_instructions:
    instruction = instruction.strip().split(' ')
    operation = instruction[0]
    if operation == 'addx':
        operand = int(instruction[1])
        cycles += 1
        if (cycles - 20) % 40 == 0:
            signal = cycles * register
            signals.append(signal)
            print(cycles)
            print(signals)
        cycles += 1
        print(f"register {register} operand {operand}")
        if (cycles - 20) % 40 == 0:
            signal = cycles * register
            signals.append(signal)
            print(cycles)
            print(signals)
        register += operand
    else:
        cycles += 1
        if (cycles - 20) % 40 == 0:
            signal = cycles * register
            signals.append(signal)
            print(cycles)
            print(signals)

print(sum(signals))
