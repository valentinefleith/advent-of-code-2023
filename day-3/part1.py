from sys import argv, exit
from typing import List, Dict


def main():
    if len(argv) != 2:
        exit("Il faut la map en argument.")
    height, width, data = parse_map(argv[1])
    map = Map(height, width, data)
    digits = map.get_digits()
    for digit in digits:
        print(digit.digits)


class Digits:
    def __init__(self, digits, x_pos, y_pos):
        self.digits = digits
        self.x_pos = x_pos
        self.y_pos = y_pos

#    def to_be_kept(self):


class Map:
    def __init__(self, height, width, data):
        self.height = height
        self.width = width
        self.data = data

    def get_digits(self):
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
