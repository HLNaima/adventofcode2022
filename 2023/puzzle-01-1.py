with open('input-01-1.txt') as input:
    elf_calories = 0
    all_elfs_calories = []
    for line in input:
        line = line.strip()
        if line:
            elf_calories += int(line.strip())
        else:
            all_elfs_calories.append(elf_calories)
            elf_calories = 0

max_calories = max(all_elfs_calories)
print(f"Max calories is {max_calories}")

sorted_all_elfs_calories = sorted(all_elfs_calories, reverse=True)
top_three_calories = sum(sorted_all_elfs_calories[:3])
print(f"Top three sum of calories is {top_three_calories}")
