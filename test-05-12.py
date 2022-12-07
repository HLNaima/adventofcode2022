
start_state = [
    ['Q', 'F', 'M', 'R', 'L', 'W', 'C', 'V'],
    ['D', 'Q', 'L'],
    ['P', 'S', 'R', 'G', 'W', 'C', 'N', 'B'],
    ['L', 'C', 'D', 'H', 'B', 'Q', 'G'],
    ['V', 'G', 'L', 'F', 'Z', 'S'],
    ['D', 'G', 'N', 'P'],
    ['D', 'Z', 'P', 'V', 'F', 'C', 'W'],
    ['C', 'P', 'D', 'M', 'S'],
    ['Z', 'N', 'W', 'T', 'V', 'M', 'P', 'C']
]


def move_from_stack(number, move_from, move_to):
    for i in range(number):
        to_move = start_state[move_from].pop()
        start_state[move_to].append(to_move)
        print(f"moved {to_move} from {move_from + 1} to {move_to +1}")


with open("input-05-12.txt", "r") as input_data_file:
    raw_moves = input_data_file.readlines()

for move in raw_moves:
    _, number, _, move_from, _, move_to = move.strip().split(' ')
    print(f"{int(number)} {int(move_from)}:{int(move_to)}")
    number = int(number)
    move_from = int(move_from) - 1
    move_to = int(move_to) - 1
    move_from_stack(number, move_from, move_to)

result = ""
for stack in start_state:
    result += str(stack[-1])

print(result)
