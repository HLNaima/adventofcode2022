def get_first_marker(buffer, marker_size):
    for i in range(len(buffer) - marker_size + 1):
        marker_map = {}
        j = 0
        while j < marker_size and buffer[i + j] not in marker_map:
            marker_map[buffer[i + j]] = 0
            j += 1

        if j == marker_size:
            return i + marker_size


with open("input-06-12.txt", "r") as input_data_file:
    raw_input = input_data_file.readlines()

input_buffer = raw_input[0]

marker_pos = get_first_marker(input_buffer, 14)

print(marker_pos)
print(input_buffer[marker_pos - 14: marker_pos])
