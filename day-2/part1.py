from sys import argv, exit
from typing import List, Dict

COLORS = {"red": 12, "green": 13, "blue": 14}


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    data = get_input_lines(argv[1])
    result = 0
    for line in data:
        id, subsets = parse_data_line(line)
        game = Game(id, subsets)
        if game.is_possible_game():
            result += game.id
    print(result)


class Game:
    def __init__(self, id, subsets):
        self.id = id
        self.subsets = subsets

    def is_possible_game(self):
        for subset in self.subsets:
            for revealed in subset:
                revealed = revealed.strip()
                if subset[revealed] > COLORS[revealed]:
                    return False
        return True


def get_input_lines(path):
    with open(path, "r") as file:
        return file.readlines()


def parse_data_line(line):
    id = get_id(line[5:])
    if id >= 100:
        subsets = get_subsets(line[9:].split(";"))
    else:
        subsets = get_subsets(line[8:].split(";"))
    return id, subsets


def get_id(line):
    i = 0
    id = ""
    while line[i].isdigit():
        id += line[i]
        i += 1
    return int(id)


def get_subsets(raw_revealed: List[str]) -> List[Dict[str, int]]:
    subsets = []
    for colors in raw_revealed:
        colors.strip()
        draw = {}
        for data in colors.split(","):
            data = data.strip().split()
            draw[data[1]] = int(data[0])
        subsets.append(draw)
    return subsets


def get_data_digits(data):
    digits = ""
    i = 0
    while data[i].isdigit():
        digits += data[i]
        i += 1
    return digits


main()
