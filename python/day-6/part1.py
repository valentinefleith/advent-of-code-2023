from sys import argv, exit
from typing import List


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    races = parse_file(argv[1])
    numbers_of_ways_to_win = []
    for race in races:
        numbers_of_ways_to_win.append(len(race.get_all_ways_to_win()))
    total = 1
    for number in numbers_of_ways_to_win:
        total *= number
    print(total)


class Race:
    def __init__(self, time, record):
        self.time = time
        self.record = record

    def get_all_ways_to_win(self):
        holding_times = []
        for holding_time in range(1, self.time):
            travelled_distance = holding_time * (self.time - holding_time)
            if travelled_distance > self.record:
                holding_times.append(holding_time)
        return holding_times


def parse_file(path):
    with open(path, "r") as inputfile:
        file = inputfile.readlines()
    times = file[0].split(":")[1].split()
    distances = file[1].split(":")[1].split()
    races = []
    for time, record in zip(times, distances):
        races.append(Race(int(time), int(record)))
    return races


if __name__ == "__main__":
    main()
