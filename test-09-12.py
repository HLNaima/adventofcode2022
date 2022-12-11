
with open("input-09-12.txt", "r") as input_data_file:
    raw_moves = input_data_file.readlines()

H = (0, 0)
T = (0, 0)

visited = set()


def move_T(H, T):
    diff_V = abs(H[0] - T[0])
    diff_H = abs(H[1] - T[1])
    direction_V = -1 if H[0] < T[0] else 1
    direction_H = -1 if H[1] < T[1] else 1

    if (diff_H == 2 and diff_V == 1) or (diff_H == 1 and diff_V == 2):
        T = (T[0] + direction_V, T[1] + direction_H)
    elif diff_V == 2:
        T = (T[0] + direction_V, T[1])
    elif diff_H == 2:
        T = (T[0], T[1] + direction_H)
    # print(f"H T {H} {T}")
    visited.add(T)
    return T


for raw_move in raw_moves:
    direction, steps = raw_move.strip().split(' ')
    steps = int(steps)
    if direction == 'R':
        for _ in range(steps):
            H = (H[0], H[1] + 1)
            T = move_T(H, T)
    elif direction == 'L':
        for _ in range(steps):
            H = (H[0], H[1] - 1)
            T = move_T(H, T)
    elif direction == 'U':
        for _ in range(steps):
            H = (H[0] + 1, H[1])
            T = move_T(H, T)
    else:
        for _ in range(steps):
            H = (H[0] - 1, H[1])
            T = move_T(H, T)

    # print(f"H {H}")
    # print(f"T {T}")
print(f"Visited {len(visited)}")
