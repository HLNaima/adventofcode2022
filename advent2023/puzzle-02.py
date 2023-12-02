import re

cubes_limit = {
    "red": 12,
    "green": 13,
    "blue": 14
}
possible_games = 0

with open('input-02.txt') as input:

    for line in input:
        game_possible = True

        line_tokens = re.split(":|;|,", line.strip())
        print(line_tokens)
        _, game_id = line_tokens[0].strip().split(' ')

        for token in line_tokens[1:]:
            cubes_number, cubes_color = token.strip().split(' ')
            if int(cubes_number) > cubes_limit[cubes_color]:
                game_possible = False
                break
        
        if game_possible:
            possible_games += int(game_id)
        

print(possible_games)

        
