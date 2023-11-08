with open("input-01-12.txt", "r") as input_data_file:
    calories = input_data_file.readlines()

elf_calories = 0
calories_per_elf = []

for raw_calorie_input in calories:
    calorie_input = raw_calorie_input.strip()
    if calorie_input:
        elf_calories += int(calorie_input, 10)
    else:
        calories_per_elf.append(elf_calories)
        elf_calories = 0

# Handle last line
if calorie_input:
    calories_per_elf.append(elf_calories)

max_calories = max(calories_per_elf)
elf_with_max_calories = calories_per_elf.index(max_calories)

calories_per_elf.sort(reverse=True)

total_max_calories = sum(calories_per_elf[0:3])

print(calories_per_elf)

print(f"Max calories => { max_calories }")
print(f"Elf with most calories => { elf_with_max_calories }")

print(f"Three max calories => { calories_per_elf[0:3] }")
print(f"Total three max => { total_max_calories }")
