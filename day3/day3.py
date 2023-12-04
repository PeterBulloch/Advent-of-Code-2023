import re

def main():
    print(part1())
    print(part2())


def get_values():
    return open("day3\day3values.txt").readlines()


def part1():
    values = get_values()

    sum = 0

    prev_symbols = None
    prev_value = ""

    for value in values:
        value = value.strip()
        symbols = list(re.finditer(r'[^\d.]', value))

        current_line_current_symbols = add_numbers_if_symbol_adjacent(value, symbols)
        value = current_line_current_symbols[0]
        sum += current_line_current_symbols[1]

        current_line_prev_symbols = add_numbers_if_symbol_adjacent(value, prev_symbols)
        value = current_line_prev_symbols[0]
        sum += current_line_prev_symbols[1]

        prev_line_current_symbols = add_numbers_if_symbol_adjacent(prev_value, symbols)
        sum += prev_line_current_symbols[1]

        prev_symbols = symbols
        prev_value = value

    return sum


def add_numbers_if_symbol_adjacent(value, symbols):
    numbers = re.finditer(r'\d+', value)

    sum = 0

    if not symbols:
        return (value, sum)
    
    for number in numbers:
        check_number = add_number_if_symbol_adjacent(value, number, symbols)
        if not check_number:
            continue

        value = check_number[0]
        sum += check_number[1]


    return (value, sum)


def add_number_if_symbol_adjacent(value, number, symbols):
    for symbol in symbols:
        # If the symbol is too far along stop processing the symbols as they are in order
        if symbol.start() > number.end() + 1:
            break

        if overlaps(number, symbol):
            replace = ""
            for _ in range(number.start(), number.end()):
                replace += "."

            return(value[:number.start()] + replace + value[number.end():], int(number.group(0)))
            


def overlaps(number, symbol):
    return max(number.start() - 1, symbol.start()) < min(number.end() + 1, symbol.end())



def part2():
    values = get_values()

    sum = 0

    prev_value = None
    prev_numbers = None
    prev_prev_numbers = None

    for value in values:
        value = value.strip()

        numbers = list(re.finditer(r'\d+', value))

        symbols = []
        if prev_value:
            symbols = list(re.finditer(r'\*', prev_value))

        all_numbers = numbers
        if prev_numbers:
            all_numbers = all_numbers + prev_numbers
        if prev_prev_numbers:
            all_numbers = all_numbers + prev_prev_numbers

        if not prev_prev_numbers is None:
            sum += get_gear_ratios(all_numbers, symbols)

        prev_prev_numbers = prev_numbers
        prev_numbers = numbers
        prev_value = value

    return sum

def get_gear_ratios(numbers, symbols):
    sum = 0

    if not symbols:
        return 0

    for symbol in symbols:
        matching_numbers = []
        for number in numbers:
            if overlaps(number, symbol):
                matching_numbers.append(number.group(0))
        if len(matching_numbers) == 2:
            sum += int(matching_numbers[0]) * int(matching_numbers[1])
        
    
    return sum


main()