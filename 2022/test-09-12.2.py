
with open("input-09-12.txt", "r") as input_data_file:
    raw_moves = input_data_file.readlines()

H = (0, 0)
T = (0, 0)

knots = [(0, 0) for _ in range(10)]

visited = set()


def move_T(H, T):
    diff_V = abs(H[0] - T[0])
    diff_H = abs(H[1] - T[1])
    direction_V = -1 if H[0] < T[0] else 1
    direction_H = -1 if H[1] < T[1] else 1

    if (diff_H == 2 and diff_V == 1) or (diff_H == 1 and diff_V == 2) or (diff_H == 2 and diff_V == 2):
        T = (T[0] + direction_V, T[1] + direction_H)
    elif diff_V == 2:
        T = (T[0] + direction_V, T[1])
    elif diff_H == 2:
        T = (T[0], T[1] + direction_H)
    print(f"H T {H} {T}")
    return T


for raw_move in raw_moves:
    direction, steps = raw_move.strip().split(' ')
    print(raw_move.strip())
    steps = int(steps)
    step_H = 0
    step_V = 0
    if direction == 'R':
        step_H = 1
    elif direction == 'L':
        step_H = -1
    elif direction == 'U':
        step_V = 1
    else:
        step_V = -1

    for _ in range(steps):
        H = knots[0]
        knots[0] = (H[0] + step_V, H[1] + step_H)
        for i in range(1, 10):
            knots[i] = move_T(knots[i-1], knots[i])
            if i == 9:
                visited.add(knots[i])

    # print(f"H {H}")
    # print(f"T {T}")
print(f"Visited {len(visited)}")
