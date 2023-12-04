import re

def main():
    print(part1())
    print(part2())


def get_values():
    return open("day2\day2values.txt").readlines()


def part1():
    values = get_values()

    possible = 0

    for value in values:
        possible += get_game_if_possible(value)

    return possible


def get_game_if_possible(value):
    split_colon = value.split(":")
    game = int(split_colon[0].replace("Game ", ""))
    sets = split_colon[1].split(";")
    for set in sets:
        if set_impossible(game, set):
            return 0
    return game


def set_impossible(game, set):
    colours = set.split(",")
    for colour in colours:
        impossible = False
        if "green" in colour:
            impossible = colour_impossible(game, "green", colour, 13)
        elif "red" in colour:
            impossible = colour_impossible(game, "red", colour, 12)
        elif "blue" in colour:
            impossible = colour_impossible(game, "blue", colour, 14)
        if impossible:
            return True
    return False


def colour_impossible(game, colour, value, limit):
    colour_value = int(value.replace(" " + colour,""))
    if colour_value > limit:
        return True
    return False


def part2():
    values = get_values()

    sum = 0

    for value in values:
        split_colon = value.split(":")
        sets = split_colon[1].split(";")

        min_green = 1
        min_red = 1
        min_blue = 1

        for set in sets:
            colours = set.split(",")
            for colour in colours:
                if "green" in colour:
                    min_green = get_bigger(min_green, colour, "green")
                elif "red" in colour:
                    min_red = get_bigger(min_red, colour, "red")
                elif "blue" in colour:
                    min_blue = get_bigger(min_blue, colour, "blue")

        sum += min_green * min_red * min_blue

    return sum

def get_bigger(min_colour, colour, replace):
    colour_value = int(colour.replace(" " + replace, ""))
    if colour_value > min_colour:
        return colour_value
    return min_colour


main()