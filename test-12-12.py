import copy, sys

sys.setrecursionlimit(10000)

def get_char_position(char):
    for i in range(lines):
        for j in range(cols):
            if elevations[i][j] == ord(char):
                return (i, j)

def is_valid(position):
    (x, y) = position
    return x >= 0 and x < lines and y >= 0 and y < cols

def explore_elevation(prev, current, acc, path):
    global found_path
    
    (current_x, current_y) = current
    (prev_x, prev_y) = prev

    current_elevation = elevations[current_x][current_y]
    prev_elevation = elevations[prev_x][prev_y]

    if current_elevation - prev_elevation <= 1:
        acc += 1
        
        if current in visited and acc >= visited[current]: 
            return
        
        visited[current] = acc
        
        path = copy.copy(path)
        path.append(current)
        

        if current == end:

            found = acc
            found_path = [chr(elevations[el[0]][el[1]]) for el in path]
            print([chr(elevations[el[0]][el[1]]) for el in path])
            print(acc)           
        else:
                        
            next_position = (current_x, current_y + 1)
            if is_valid(next_position):
                explore_elevation(current, next_position, acc, path)
            
            next_position = (current_x + 1, current_y)
            if is_valid(next_position):
                explore_elevation(current, next_position, acc, path)
            
            next_position = (current_x - 1, current_y)
            if is_valid(next_position):
                explore_elevation(current, next_position, acc, path)
            
            next_position = (current_x, current_y - 1)
            if is_valid(next_position):
                explore_elevation(current, next_position, acc, path)




with open("input-12-12.txt", "r") as input_data_file:
    elevations = input_data_file.readlines()

for i in range(len(elevations)):
    elevations[i] = [ord(elevation) for elevation in elevations[i].strip()]

lines = len(elevations)
cols = len(elevations[0])

start = get_char_position('S')
end = get_char_position('E')

(x, y) = start
elevations[x][y] = ord('a')
(x, y) = end
elevations[x][y] = ord('z')

visited = {start: True}
path = [start]
found_path=[]
acc = 0

        
(x, y) = start

next_position = (x, y + 1)
if is_valid(next_position):
    explore_elevation(start, next_position, acc, path)

next_position = (x + 1, y)
if is_valid(next_position):
    explore_elevation(start, next_position, acc, path)

next_position = (x - 1, y)
if is_valid(next_position):
    explore_elevation(start, next_position, acc, path)

next_position = (x, y - 1)
if is_valid(next_position):
    explore_elevation(start, next_position, acc, path)
