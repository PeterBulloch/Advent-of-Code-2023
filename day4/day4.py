import re

def main():
    print(part1())
    print(part2())


def get_values():
    return open("day4\day4values.txt").readlines()


def part1():
    values = get_values()

    sum = 0

    for value in values:
        split_colon = value.split(":")
        split_pipe = split_colon[1].split("|")
        winners = split_pipe[0].strip().replace("  ", " ").split(" ")
        numbers = split_pipe[1].strip().replace("  ", " ").split(" ")

        wins = -1

        for number in numbers:
            if number in winners:
                wins += 1

        if wins == -1:
            continue

        sum += pow(2, wins)

    return sum



def part2():
    values = get_values()

    sum = 0

    # All cards have one copy by default
    copies = [1] * len(values)

    for index, value in enumerate(values):
        split_colon = value.split(":")
        split_pipe = split_colon[1].split("|")
        winners = split_pipe[0].strip().replace("  ", " ").split(" ")
        numbers = split_pipe[1].strip().replace("  ", " ").split(" ")

        wins = 0
        for number in numbers:
            if number in winners:
                wins += 1
        
        # Process once for each copy
        for _ in range(copies[index]):
            for win in range(wins):
                copies[index + win + 1] = copies[index + win + 1] + 1

    for copy in copies:
        sum += copy

    return sum


main()