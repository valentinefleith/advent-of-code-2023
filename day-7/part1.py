from sys import argv, exit

TYPES = ["five of a kind",
         "four of a kind",
         "full house",
         "three of a kind",
         "two pairs",
         "one pair",
         "high card"]

CARDS = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    hands = load_input(argv[1])
    sorted_hands = sort_hands_by_strength(hands)
    total_winning = 0
    for i, hand in enumerate(sorted_hands):
        print(hand.cards, hand.h_type.strength, i + 1)
        total_winning += (i + 1) * int(hand.bid)
    print(total_winning)


class Hand:
    def __init__(self, cards, bid, h_type):
        self.cards = cards
        self.bid = bid
        self.h_type = h_type


class Type:
    """
    Every type is assigned to a number, which refers to
    the strength of the type.
    0 is the strongest, 5 the weakest.
    """
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


def load_input(path):
    hands = []
    with open(path, "r") as input_file:
        for line in input_file:
            cards = line.split()[0]
            bid = line.split()[1].strip()
            h_type = parse_hand_type(cards)
            hands.append(Hand(cards, bid, h_type))
    return hands


def sort_hands_by_strength(hands):
    hands.sort(key=lambda x: (x.h_type.strength, [CARDS.index(card) for card in x.cards]), reverse=True)
    return hands


def parse_hand_type(cards):
    if cards == len(cards) * cards[0]:
        return Type(TYPES[0], 0)
    if cards.count(cards[0]) == 4 or cards.count(cards[1]) == 4:
        return Type(TYPES[1], 1)
    nb_of_different_cards = len(set(cards))
    if nb_of_different_cards == 2:
        return Type(TYPES[2], 2)
    for i in range(3):
        if cards.count(cards[i]) == 3:
            return Type(TYPES[3], 3)
    return Type(TYPES[nb_of_different_cards + 1], nb_of_different_cards + 1)


if __name__ == "__main__":
    main()
