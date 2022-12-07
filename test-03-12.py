def get_priority(item):
    priority = ord(item)
    if priority >= 97:
        priority -= 96
    else:
        priority -= 38

    return priority


def get_common_items(compartment_1, compartment_2):
    common_items = []
    for item in compartment_1:
        if item in compartment_2:
            item_priority = get_priority(item)
            if item_priority not in common_items:
                common_items.append(item_priority)

    return common_items


with open("input-03-12.txt", "r") as input_data_file:
    raw_rucksacks = input_data_file.readlines()

wrong_items = []
for rucksack in raw_rucksacks:
    rucksack = rucksack.strip()

    compartment_size = len(rucksack)//2
    compartment_1 = rucksack[:compartment_size]
    compartment_2 = rucksack[compartment_size:]

    wrong_items.extend(get_common_items(compartment_1, compartment_2))

print(wrong_items)
print(sum(wrong_items))
