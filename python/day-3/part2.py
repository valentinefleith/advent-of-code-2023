from sys import argv, exit
from typing import List, Dict

from part1 import parse_map, Map, Digits


def main():
    if len(argv) != 2:
        exit("Il faut la map en argument.")
    height, width, data = parse_map(argv[1])
    map = Map(height, width, data)
    digits = map.get_digits()
    gears = find_gears(map, digits)
    result = 0
    for gear in gears:
        multiplication = 1
        for number in gear.digits_near:
            multiplication *= int(number.digits)
        result += multiplication
    print(result)


class Gear:
    def __init__(self, x_pos, y_pos, digits_near):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.digits_near = digits_near


def find_gears(map: Map, digits: List[Digits]) -> List[Gear]:
    gears = []
    for i in range(map.height):
        for j in range(map.width):
            if map.data[i][j] == "*":
                near_digits = find_digits_near(digits, i, j)
                if len(near_digits) == 2:
                    gears.append(Gear(i, j, near_digits))
    return gears


def find_digits_near(digits: List[Digits], x_pos, y_pos) -> List[Digits]:
    near_digits = []
    for digit in digits:
        if x_pos in range(digit.x_pos - 1, digit.x_pos + 2):
            if y_pos in range(digit.y_pos[0] - 1, digit.y_pos[-1] + 2):
                near_digits.append(digit)
    return near_digits


if __name__ == "__main__":
    main()
