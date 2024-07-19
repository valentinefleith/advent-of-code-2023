from sys import argv, exit
from typing import List, Dict


def main():
    if len(argv) != 2:
        exit("Il faut la map en argument.")
    height, width, data = parse_map(argv[1])
    map = Map(height, width, data)
    digits = map.get_digits()
    adjacent_to_symbol = map.get_adjacent_to_symbols(digits)
    result = 0
    for dig in adjacent_to_symbol:
        result += int(dig.digits)
    print(result)


class Digits:
    def __init__(self, digits, x_pos, y_pos):
        self.digits = digits
        self.x_pos = x_pos
        self.y_pos = y_pos


class Map:
    def __init__(self, height, width, data):
        self.height = height
        self.width = width
        self.data = data

    def get_digits(self) -> List[Digits]:
        digits = []
        for i in range(self.height):
            j = 0
            while j < self.width:
                if self.data[i][j].isdigit():
                    dig = self.get_entire_numbers(i, j)
                    digits.append(dig)
                    j += len(dig.digits)
                j += 1
        return digits

    def get_entire_numbers(self, x_pos, y_pos):
        y = []
        digits = ""
        while self.data[x_pos][y_pos].isdigit():
            digits += self.data[x_pos][y_pos]
            y.append(y_pos)
            y_pos += 1
        return Digits(digits, x_pos, y)

    def get_adjacent_to_symbols(self, digits: List[Digits]) -> List[Digits]:
        adjacents = []
        for digit in digits:
            if self.is_valid(digit):
                adjacents.append(digit)
        return adjacents

    def is_valid(self, digit: Digits) -> bool:
        i = digit.x_pos - 1
        while i <= digit.x_pos + 1:
            if i < 0:
                i += 1
            if i >= self.height:
                break
            j = digit.y_pos[0] - 1
            while j <= digit.y_pos[-1] + 1:
                if j < 0:
                    j += 1
                if j >= self.width:
                    continue
                if not self.data[i][j].isdigit() and self.data[i][j] not in ".\n":
                    return True
                j += 1
            i += 1
        return False


def parse_map(path):
    with open(path, "r") as input:
        map = input.readlines()
    height = len(map)
    width = len(map[0])
    data = []
    for line in map:
        data.append(list(line))
    return height, width, data


if __name__ == "__main__":
    main()
