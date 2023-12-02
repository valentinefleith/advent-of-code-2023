from sys import argv, exit
from typing import List, Dict

from part1 import get_input_lines, parse_data_line


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    data = get_input_lines(argv[1])
    fewest = []
    for line in data:
        id, subsets = parse_data_line(line)
        game = Game(id, subsets)
        fewest.append(game.get_fewest_cubes())
    result = calculate_sum_of_powers(fewest)
    print(result)


class Game:
    def __init__(self, id, subsets):
        self.id = id
        self.subsets = subsets

    def get_fewest_cubes(self) -> Dict[str, int]:
        fewest = {"blue": 0, "red": 0, "green": 0}
        for subset in self.subsets:
            for color in subset:
                if subset[color] > fewest[color]:
                    fewest[color] = subset[color]
        return fewest


def calculate_sum_of_powers(fewest: List[Dict[str, int]]):
    result = 0
    for game in fewest:
        power = 1
        for number in game.values():
            power *= number
        result += power
    return result


main()
