from sys import argv, exit
from typing import List
import numpy as np

from part1 import parse_maps, Map, Conversion 


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    pairs = parse_first_line(argv[1])
    maps = parse_maps(argv[1])
    intervals = []
    for start, number in pairs.items():
        intervals.append([start, start + number])
    print(intervals)
    locations = []
    for interval in intervals:
        locations.append(convert_intervals_to_locations(interval, maps))
    print(locations)
    #locations = np.array([locations])
    #print(locations.min())


def convert_intervals_to_locations(interval, maps):
    new_intervals = [interval]
    for inter in new_intervals:
        for map in maps:
            interval = new_intervals
            new_intervals = []
            for conversion in map.data:
                print(f"interval : {inter}")
                case = get_interval_case(inter, conversion)
                new_intervals.append(get_new_intervals(inter, case, conversion))
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
