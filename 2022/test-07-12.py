def get_dir_size(tree, directory):
    size = tree[directory]["size"]
    if len(tree[directory]["dirs"]) > 0:
        for dir_ in tree[directory]["dirs"]:
            dir_ = directory + "/" + dir_
            size += get_dir_size(tree, dir_)

    return size


with open("input-07-12.txt", "r") as input_data_file:
    raw_terminal_output = input_data_file.readlines()

tree = {}
i = 0
parent_dir = ''
while i < len(raw_terminal_output):
    line = raw_terminal_output[i]
    # print(line)
    _, _, directory = line.strip().split(' ')
    if directory == '..':
        parent_dir = tree[parent_dir]["parent"]
        i += 1
    else:
        key = parent_dir + "/" + directory
        tree[key] = {"parent": parent_dir, "size": 0, "dirs": []}
        i += 2
        while i < len((raw_terminal_output)) and raw_terminal_output[i][0] != '$':
            line = raw_terminal_output[i]
            # print(line)
            ls_line = line.strip().split(' ')
            if ls_line[0] == 'dir':
                tree[key]["dirs"].append(ls_line[1])
            else:
                tree[key]["size"] += int(ls_line[0])

            i += 1
        # print(tree[key])
        parent_dir = parent_dir + "/" + directory

total = 0
sizes = []
size_to_free = 30000000 - (70000000 - get_dir_size(tree, '//'))
for directory in tree:
    dir_size = get_dir_size(tree, directory)
    print(f"{directory} {dir_size}")
    if dir_size >= size_to_free:
        sizes.append(dir_size)
    if (dir_size <= 100000):
        print(tree[directory])
        total += dir_size

print(total)
print(min(sizes))
