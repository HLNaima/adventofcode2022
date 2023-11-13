with open('input-03.txt') as input:
    priorities_sum = 0
    for line in input:
        rucksuck = line.strip()
        n = len(rucksuck)
        compartment_1, compartment_2 = rucksuck[:n//2], rucksuck[n//2:]

        common_items = set()
        for item_type_c1 in compartment_1:
            for item_type_c2 in compartment_2:
                if item_type_c1 == item_type_c2:
                    if item_type_c1 not in common_items:
                        common_items.add(item_type_c1)
                        priorities_sum += (ord(item_type_c1) - 96) if ord(item_type_c1) >= 97 else (ord(item_type_c1) - 65 + 27)
        
    print(f"Sum of priorities = {priorities_sum}")    

with open('input-03.txt') as input:
    i, priorities_sum = 0, 0
    lines = input.readlines()
    for i in range(0, len(lines), 3):
        elf_1, elf_2, elf_3 = set(lines[i].strip()), set(lines[i+1].strip()), set(lines[i+2].strip())

        # intersection = elf_1.intersection(elf_2).intersection(elf_3)
        # item_type = intersection.pop()

        for item_type in elf_1:
            if item_type in elf_2 and item_type in elf_3:
                priorities_sum += (ord(item_type) - 96) if ord(item_type) >= 97 else (ord(item_type) - 65 + 27)


    print(f"Sum of priorities = {priorities_sum}")    
