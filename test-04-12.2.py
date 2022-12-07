def does_overlap(first_pair, second_pair):
    first_pair_1 = int(first_pair[0])
    first_pair_2 = int(first_pair[1])

    second_pair_1 = int(second_pair[0])
    second_pair_2 = int(second_pair[1])

    for section in range(first_pair_1, first_pair_2 + 1):
        if section >= second_pair_1 and section <= second_pair_2:
            return True
    return False


with open("input-04-12.txt", "r") as input_data_file:
    raw_assignment_pairs = input_data_file.readlines()

number_overlaps = 0
for assignment_pair in raw_assignment_pairs:
    first_pair, second_pair = assignment_pair.strip().split(",")
    first_pair = first_pair.split("-")
    second_pair = second_pair.split("-")

    if does_overlap(first_pair, second_pair):
        number_overlaps += 1

print(number_overlaps)
