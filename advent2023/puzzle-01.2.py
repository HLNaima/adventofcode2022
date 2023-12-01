text_to_digit = {
    "one": '1',
    "two": '2',
    "three": '3',
    "four": '4',
    "five": '5',
    "six": '6',
    "seven": '7',
    "eight": '8',
    "nine": '9'
}

with open('input-01.2.txt') as input:
    calibration_sum = 0
    for line in input:
        calibration_line = line.strip()
        digits = []
        for i in range(0, len(calibration_line)):
            char = calibration_line[i]
            if ord(char) >= 48 and ord(char) <= 57:
                digits.append(char)
            elif calibration_line[i:i + 3] in ['one', 'two', 'six']:
                digits.append(text_to_digit[calibration_line[i:i + 3]])
            elif calibration_line[i:i + 4] in ['four', 'five', 'nine']:
                digits.append(text_to_digit[calibration_line[i:i + 4]])
            elif calibration_line[i:i + 5] in ['three', 'seven', 'eight']:
                digits.append(text_to_digit[calibration_line[i:i + 5]])

        print(digits)
        calibration = f"{digits[0]}{digits[-1]}"
        calibration_sum += int(calibration)

print(calibration_sum)
