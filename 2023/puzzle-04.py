nbr_overlaps = 0
with open('input-04.txt') as input:
    for line in input:
        pairs = line.strip().split(',')
        elf1, elf2 = [[int(id) for id in pair.split('-')] for pair in pairs]
        print(f"elf1={elf1}, elf2={elf2}")

        if ((elf1[0] >= elf2[0]) and (elf1[1] <= elf2[1])) or ((elf1[0] <= elf2[0]) and (elf1[1] >= elf2[1])):
            nbr_overlaps += 1
        
print(nbr_overlaps)
