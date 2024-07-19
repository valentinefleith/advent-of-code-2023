import sys

from part1 import parse_line


def main():
    if len(sys.argv) != 2:
        sys.exit("Il faut l'input en argument.")
    cards = []
    numero = 1
    with open(sys.argv[1], "r") as file:
        for line in file:
            winning_numbers, my_numbers = parse_line(line)
            cards.append(Card(numero, winning_numbers, my_numbers))
            numero += 1
    number_of_cards = get_number_of_instances(cards)
    total = sum(number_of_cards.values())
    print(total)


class Card:
    def __init__(self, numero, winning_numbers, my_numbers):
        self.numero = numero
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    def get_number_of_winning(self):
        winning = []
        for number in self.my_numbers:
            if number in self.winning_numbers:
                winning.append(number)
        return len(winning)


def get_number_of_instances(cards):
    number_of_instances = {}
    for card in cards:
        number_of_instances[card.numero] = 1
    for card in cards:
        numero = card.numero
        for number_of_copies in range(number_of_instances[card.numero]):
            numero = card.numero
            for number_of_wins in range(card.get_number_of_winning()):
                number_of_instances[numero + 1] += 1
                numero += 1
    return number_of_instances


if __name__ == "__main__":
    main()
