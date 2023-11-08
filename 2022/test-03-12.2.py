def get_priority(item):
    priority = ord(item)
    if priority >= 97:
        priority -= 96
    else:
        priority -= 38

    return priority


def get_badge_priority(group_rucksacks):
    for item in group_rucksacks[0]:
        if item in group_rucksacks[1] and item in group_rucksacks[2]:
            return get_priority(item)


with open("input-03-12.txt", "r") as input_data_file:
    raw_rucksacks = input_data_file.readlines()

sum_badges = 0
i = 0
while i < len(raw_rucksacks):
    group_rucksacks = raw_rucksacks[i:i+3]
    i += 3

    # group_rucksacks = list(map(lambda item: item.strip(), group_rucksacks))
    sum_badges += get_badge_priority(group_rucksacks)

print(sum_badges)
