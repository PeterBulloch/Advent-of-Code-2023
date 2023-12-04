import re


def get_values():
    return open("day1\day1values.txt").readlines()


def part1():
    values = get_values()
    sum = 0
    for value in values:
        digits = re.findall(r'\d', value)
        calibration = digits[0] + "" + digits[len(digits)-1]
        sum += int(calibration)
    return sum

def part2():
    values = get_values()
    sum = 0
    text_digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for value in values:
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', value)
        first = digits[0] if digits[0].isnumeric() else text_digits.index(digits[0])
        last = digits[len(digits)-1] if digits[len(digits)-1].isnumeric() else text_digits.index(digits[len(digits)-1])
        calibration = str(first) + "" + str(last)
        sum += int(calibration)
    return sum



print(part1())
print(part2())