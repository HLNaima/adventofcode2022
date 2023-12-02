import re

game_power = 0

with open('input-02.txt') as input:

    for line in input:
        cubes_limit = {
            "red": 0,
            "green": 0,
            "blue": 0
        }

        line_tokens = re.split(":|;|,", line.strip())
        print(line_tokens)

        for token in line_tokens[1:]:
            cubes_number, cubes_color = token.strip().split(' ')
            if int(cubes_number) > cubes_limit[cubes_color]:
                cubes_limit[cubes_color] = int(cubes_number)
        

        game_power += cubes_limit["red"] * cubes_limit["green"] * cubes_limit["blue"]
        

print(game_power)

        
