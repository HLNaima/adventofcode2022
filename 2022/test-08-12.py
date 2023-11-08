def print_grid(grid):
    for line in grid:
        print(line)


def get_dist(i, row):
    k = i + 1
    dist = 0
    while k < len(row) and row[k] < row[i]:
        dist += 1
        k += 1
    if k < len(row):
        dist += 1
    return dist


with open("input-08-12.txt", "r") as input_data_file:
    raw_tree_grid = input_data_file.readlines()

row_number = len(raw_tree_grid)
col_number = len(raw_tree_grid[0].strip())

grid = [[0 for _ in range(col_number)] for _ in range(row_number)]

number_trees = 0
for row in range(1, row_number - 1):
    row_trees = raw_tree_grid[row].strip()

    j = 1
    while j < col_number:
        if row_trees[j] > max(row_trees[:j]):
            grid[row][j] = 1
        j += 1

    k = col_number - 2
    while k >= 0:
        if row_trees[k] > max(row_trees[k + 1:]):
            grid[row][k] = 1
        k -= 1

for col in range(1, col_number - 1):
    j = 1
    while j < row_number - 1:
        if raw_tree_grid[j][col] > max([raw_tree_grid[row][col] for row in range(j)]):
            grid[j][col] = 1
        j += 1

    k = row_number - 2
    while k >= 0:
        if raw_tree_grid[k][col] > max([raw_tree_grid[row][col] for row in range(k + 1, row_number)]):
            grid[k][col] = 1
        k -= 1

total = 2 * (col_number + row_number - 2)
for i in range(1, row_number - 1):
    total += sum(grid[i][1: col_number - 1])

print(f"Total visible trees {total}")

distances = []
for i in range(1, row_number - 1):
    for j in range(1, col_number - 1):
        if grid[i][j] == 1:

            row = [int(elm) for elm in raw_tree_grid[i].strip()]
            right = get_dist(j, row)
            n = len(row)
            row = [row[n-1-i] for i in range(n)]
            left = get_dist(n - j - 1, row)

            row = [int(raw_tree_grid[k][j]) for k in range(row_number)]
            down = get_dist(i, row)
            n = len(row)
            row = [row[n-1-i] for i in range(n)]
            up = get_dist(n - i - 1, row)

            distance = up * down * right * left

            distances.append(distance)
print(f"Max distance {max(distances)}")
