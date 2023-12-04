import sys


def main():
    if len(sys.argv) != 2:
        sys.exit("Il faut l'input en argument.")
    cards = []
    with open(sys.argv[1], "r") as file:
        for line in file:
            winning_numbers, my_numbers = parse_line(line)
            cards.append(Card(winning_numbers, my_numbers))
    result = 0
    for card in cards:
        result += card.get_card_value()
    print(result)


class Card:
    def __init__(self, winning_numbers, my_numbers):
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    def get_card_value(self):
        winning = []
        for number in self.my_numbers:
            if number in self.winning_numbers:
                winning.append(number)
        if not winning:
            return 0
        score = 1
        for number in winning:
            score *= 2
        return score / 2


def parse_line(line):
    start_index = find_index_sep(line, ":") + 1
    end_index = find_index_sep(line, "|")
    winning_numbers = line[start_index:end_index].strip().split()
    start_index = end_index + 2
    end_index = -1
    my_numbers = line[start_index:end_index].strip().split()
    return winning_numbers, my_numbers


def find_index_sep(line, sep):
    i = 0
    while line[i] != sep and i < len(line):
        i += 1
    return i


if __name__ == "__main__":
    main()
