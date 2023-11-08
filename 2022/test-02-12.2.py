def get_round_score(other_shape, played_shape):

    if other_shape == 'A':
        other = 1
    elif other_shape == 'B':
        other = 2
    else:
        other = 3

    if played_shape == 'X':
        played = 0
    elif played_shape == 'Y':
        played = 1
    else:
        played = 2

    score = (other + 1 + played) % 3 + 1 + 3 * played
    # if played_shape == "Y":
    #     score = other + 3
    # elif played_shape == "Z":
    #     score = 6
    #     if other == 3:
    #         score += 1
    #     elif other == 2:
    #         score += 3
    #     else:
    #         score += 2
    # else:
    #     if other == 3:
    #         score = 2
    #     elif other == 2:
    #         score = 1
    #     else:
    #         score = 3

    return score


with open("input-02-12.txt", "r") as input_data_file:
    raw_strategy_rounds = input_data_file.readlines()

total_score = 0
for s_round in raw_strategy_rounds:
    o_shape, p_shape = s_round.strip().split(" ")
    total_score += get_round_score(o_shape, p_shape)

print(f"Total score => { total_score }")
