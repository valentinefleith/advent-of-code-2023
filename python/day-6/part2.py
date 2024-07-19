from sys import argv, exit
from typing import List

from part1 import Race


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    race = parse_file(argv[1])
    numbers_of_ways_to_win = len(race.get_all_ways_to_win())
    print(numbers_of_ways_to_win)


def parse_file(path):
    with open(path, "r") as inputfile:
        file = inputfile.readlines()
    time = file[0].split(":")[1].replace(" ", "")
    record = file[1].split(":")[1].replace(" ", "")
    races = Race(int(time), int(record))
    return races


if __name__ == "__main__":
    main()
