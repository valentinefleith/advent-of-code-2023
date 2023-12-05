from sys import argv, exit
from typing import List

from part1 import parse_maps, Map, Conversion 


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    pairs = parse_first_line(argv[1])
    intervals = []
    for start, number in pairs.items():
        intervals.append([start, start + number])
    print(intervals)
    locations = convert_intervals_to_locations(intervals, argv[1])
    print(min(locations))


def convert_intervals_to_locations(intervals, path):
    new_intervals = intervals
    maps = parse_maps(path)
    for map in maps:
        for conversion in map.data:
            intervals = new_intervals
            for interval in intervals:
                print(interval)
                case = get_interval_case(interval, conversion)
                print(case)
                new_intervals.extend(get_new_intervals(interval, case, conversion))
    return new_intervals


def get_new_intervals(interval, case, conversion):
    transformation = conversion.dest - conversion.src
    if case == 1:
        return [interval[0] + transformation, interval[1] + transformation]
    if case == 2:
        return [[interval[0] + transformation, conversion.src + conversion.quantity - 1 + transformation], [conversion.src + conversion.quantity, interval[1]]]
    if case == 3:
        return [[interval[0], conversion.src - 1], [conversion.src + transformation, interval[1] + transformation]]
    if case == 4:
        return [[interval[0], conversion.src - 1], [conversion.src + transformation, conversion.src + conversion.quantity - 1+ transformation], [conversion.src + conversion.quantity, interval[1]]]
    return interval


def get_interval_case(interval, conversion):
    if conversion.src <= interval[0]:
        if conversion.src + conversion.quantity >= interval[1]:
            return 1
        if interval[0] < conversion.src + conversion.quantity < interval[1]:
            return 2
    if interval[0] < conversion.src < interval[1]:
        if conversion.src + conversion.quantity >= interval[1]:
            return 3
        if conversion.src + conversion.quantity < interval[1]:
            return 4
    return 0


def parse_first_line(path):
    with open(path, "r") as almanach:
        line = almanach.readline()
        data = line.split(":")[1].split()
    converted = [int(seed) for seed in data]
    pairs = {}
    for i in range(0, len(converted) - 1, 2):
        pairs[converted[i]] = converted[i + 1]
    return pairs


if __name__ == "__main__":
    main()
