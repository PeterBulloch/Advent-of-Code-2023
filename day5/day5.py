import sys

def main():
    print(part1())
    print(part2_ranges())


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
            mapped_seed = map_forwards(seed[0], value)
            if mapped_seed != seed[0]:
                seeds[index] = (mapped_seed, True)

    lowest = sys.maxsize

    for seed in seeds:
        if seed[0] < lowest:
            lowest = seed[0]

    return lowest

def map_forwards(seed, value):
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
            mapped_seed = map_forwards(seed[0], value)
            if mapped_seed != seed[0]:
                seeds[index] = (mapped_seed, True)

    lowest = sys.maxsize

    for seed in seeds:
        if seed[0] < lowest:
            lowest = seed[0]

    return lowest

def part2_backwards():
    values = get_values()

    seed_value = values[0]
    seeds = list(map(int,seed_value.strip().split(":")[1].strip().replace("  ", " ").split(" ")))
    values.pop(0)
    values.reverse()

    # Start from 0 and map backwards to find the first seed match
    for location in range(sys.maxsize):
        number = location
        # Flag to prevent the same map from being used twice on the value
        map_processed = False
        for value in values:
            if value.strip() == "":
                continue
            if  "map:" in value:
                # Reset it so the value can be processed by the next map
                map_processed = False
                continue

            if map_processed:
                continue
            
            mapped_number = map_backwards(number, value)
            if mapped_number != number:
                map_processed = True
                number = mapped_number
        
        for index, seed in enumerate(seeds):
            # Skip evens
            if index % 2 == 0:
                continue
            # If the processed location matches one of the seeds return the original location
            if number >= seeds[index - 1] and number <= seeds[index - 1] + seed:
                return location


def map_backwards(location, value):
    map_numbers = value.strip().replace("  ", " ").split(" ")
    destination = int(map_numbers[0])
    source = int(map_numbers[1])
    length = int(map_numbers[2])

    # If it's outside of the map range then leave it alone
    if location < destination or length < location - destination:
        return location
    
    # Otherwise map it
    return source + location - destination

def part2_ranges():
    values = get_values()

    # Initialise tuples for the ranges
    seeds = []
    seed_value = values[0]
    initial_seeds = list(map(int,seed_value.strip().split(":")[1].strip().replace("  ", " ").split(" ")))
    for index, seed in enumerate(initial_seeds):
        # Skip evens
        if index % 2 == 0:
            continue
        seeds.append(((initial_seeds[index - 1], seed), False))

    # Remove the seeds line
    values.pop(0)

    for value in values:
        if value.strip() == "":
            continue
        if  "map:" in value:
            # Reset the seeds so they get processed by the new map
            for index, seed in enumerate(seeds):
                seeds[index] = (seed[0], False)
            continue

        map_numbers = value.strip().replace("  ", " ").split(" ")
        destination = int(map_numbers[0])
        source = int(map_numbers[1])
        length = int(map_numbers[2])
        
        for index, seed in enumerate(seeds):
            # Don't re-process seeds within a map
            if seed[1]:
                continue

            seed_start = seed[0][0]
            seed_length = seed[0][1]

            # If the seed range is outside of the map range then just skip it
            if seed_start + seed_length < source or seed_start > source + length:
                continue

            # Separate the part of the seed range lower than the map if there is any
            seed_length_below_source = source - seed_start
            if seed_length_below_source > 0:
                seeds.insert(index + 1, ((seed_start, seed_length_below_source - 1), False))
                seed_start = source
                seed_length = seed_length - seed_length_below_source

            # Separate the part of the seed range higher than the map
            seed_length_above_source = (seed_start + seed_length) - (source + length)
            if seed_length_above_source > 0:
                seeds.insert(index + 1, ((seed_start + length + 1, seed_length_above_source), False))
                seed_length = seed_length - seed_length_above_source

            # Map the remaining seed range
            seeds[index] = ((destination + seed_start - source, seed_length), True)

    lowest = sys.maxsize

    for seed in seeds:
        if seed[0][0] < lowest:
            lowest = seed[0][0]

    return lowest



main()