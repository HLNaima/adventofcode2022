with open('input-01.txt') as input:
    calibration_sum = 0
    for line in input:
        calibration_line = line.strip()
        digits = []
        for char in calibration_line:
            if ord(char) >= 48 and ord(char) <= 57:
                digits.append(char)
        print(digits)
        calibration = f"{digits[0]}{digits[-1]}"
        calibration_sum += int(calibration)

print(calibration_sum)
