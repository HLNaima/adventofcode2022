def get_round_score(other_shape, played_shape):

    if other_shape == 'A':
        other = 1
    elif other_shape == 'B':
        other = 2
    else:
        other = 3

    if played_shape == 'X':
        result = 0
    elif played_shape == 'Y':
        result = 1
    else:
        result = 2

    playedmod = (result + other + 1) % 3
    # if playedmod == 0:
    #     playedmod = 3

    score = (result * 3) + (result + other + 1) % 3 + 1

    print(f"playedmod => { playedmod }")
    print(f"result => { result }")
    print(f"score => { score }")
    return score


with open("input-02-12.txt", "r") as input_data_file:
    raw_strategy_rounds = input_data_file.readlines()

total_score = 0
for s_round in raw_strategy_rounds:
    o_shape, p_shape = s_round.strip().split(" ")
    total_score += get_round_score(o_shape, p_shape)

print(f"Total score => { total_score }")
