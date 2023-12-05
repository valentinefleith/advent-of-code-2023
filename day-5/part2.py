from sys import argv, exit
from typing import List


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    pairs = parse_first_line(argv[1])
    print(pairs)
    candidates = []
    for start, number in pairs.items():
        numbers_to_test = []
        for i in range(number):
            numbers_to_test.append(start + i)
        locations = []
        for seed in numbers_to_test:
            locations.append(convert_seed_to_location(seed, argv[1]))
            print(locations)
        candidates.append(min(locations))
    print(min(candidates))



def convert_seed_to_location(seed, path):
    location = seed
    maps = parse_maps(path)
    for map in maps:
        for conversion in map.data:
            if location in range(conversion.src, conversion.src + conversion.quantity):
                location = convert_location(location, conversion)
                break
    return location


def convert_location(location, conversion):
    location += (conversion.dest - conversion.src)
    return location


def parse_first_line(path):
    with open(path, "r") as almanach:
        line = almanach.readline()
        data = line.split(":")[1].split()
    converted = [int(seed) for seed in data]
    pairs = {}
    for i in range(0, len(converted) - 1, 2):
        pairs[converted[i]] = converted[i + 1]
    return pairs


class Conversion:
    def __init__(self, dest, src, quantity):
        self.dest = dest
        self.src = src
        self.quantity = quantity


class Map:
    def __init__(self, name, data: List[Conversion]):
        self.name = name
        self.data = data


def parse_maps(path):
    maps = []
    with open(path, "r") as file:
        almanach = file.readlines()
    for index, line in enumerate(almanach):
        if index == 0:
            continue
        if ":" in line:
            index_end_of_data = get_index_end_of_data(almanach, index)
            name = line.split()[0]
            data = get_list_of_conversions(almanach, index, index_end_of_data)
            maps.append(Map(name, data))
    return maps


def get_list_of_conversions(almanach, index, index_end):
    data = []
    for i in range(index + 1, index_end):
        line = almanach[i].split()
        dest = int(line[0])
        src = int(line[1])
        quantity = int(line[2])
        data.append(Conversion(dest, src, quantity))
    return data


def get_index_end_of_data(almanach, index):
    while index < len(almanach) and almanach[index] != "\n":
        index += 1
    return index


if __name__ == "__main__":
    main()
