import sys

def main():
    print(part1())
    print(part2())


def get_values():
    return open("day5/day5values.txt").readlines()


def part1():
    values = get_values()

    seeds = []

    for value in values:
        if "seeds:" in value:
            initial_seeds = value.strip().split(":")[1].strip().replace("  ", " ").split(" ")
            for seed in initial_seeds:
                # Initialise the seeds to have not been processed by a map
                seeds.append((int(seed), False))
            continue
        if value.strip() == "":
            continue
        if "map:" in value:
            # Reset the seeds so they get processed by the new map
            for index, seed in enumerate(seeds):
                seeds[index] = (seed[0], False)
            continue

        for index, seed in enumerate(seeds):
            # Don't process already mapped seeds
            if seed[1]:
                continue
            mapped_seed = map(seed[0], value)
            if mapped_seed != seed[0]:
                seeds[index] = (mapped_seed, True)

    lowest = sys.maxsize

    for seed in seeds:
        if seed[0] < lowest:
            lowest = seed[0]

    return lowest

def map(seed, value):
    map_numbers = value.strip().replace("  ", " ").split(" ")
    destination = int(map_numbers[0])
    source = int(map_numbers[1])
    length = int(map_numbers[2])

    # If it's outside of the map range then leave it alone
    if seed < source or length < seed - source:
        return seed
    
    # Otherwise map it
    return destination + seed - source




def part2():
    values = get_values()

    seeds = []

    for value in values:
        if "seeds:" in value:
            initial_seeds = value.strip().split(":")[1].strip().replace("  ", " ").split(" ")
            for index, initial_seed in enumerate(initial_seeds):
                # Skip evens
                if index % 2 == 0:
                    continue
                for seed in range(int(initial_seed)):
                    # Initialise the seeds to have not been processed by a map
                    seeds.append((int(initial_seeds[index - 1]) + seed, False))
            continue
        if value.strip() == "":
            continue
        if "map:" in value:
            # Reset the seeds so they get processed by the new map
            for index, seed in enumerate(seeds):
                seeds[index] = (seed[0], False)
            continue

        for index, seed in enumerate(seeds):
            # Don't process already mapped seeds
            if seed[1]:
                continue
            mapped_seed = map(seed[0], value)
            if mapped_seed != seed[0]:
                seeds[index] = (mapped_seed, True)

    lowest = sys.maxsize

    for seed in seeds:
        if seed[0] < lowest:
            lowest = seed[0]

    return lowest


main()