from sys import argv, exit

from part1 import parse_hand_type, sort_hands_by_strength, Hand, Type, TYPES


CARDS = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


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



def load_input(path):
    hands = []
    with open(path, "r") as input_file:
        for line in input_file:
            cards = line.split()[0]
            bid = line.split()[1].strip()
            h_type = parse_hand_type(cards)
            if "J" in cards:
                h_type = find_better_match_with_J(cards, h_type)
            hands.append(Hand(cards, bid, h_type))
    return hands


def sort_hands_by_strength(hands):
    hands.sort(key=lambda x: (x.h_type.strength, [CARDS.index(card) for card in x.cards]), reverse=True)
    return hands



def find_better_match_with_J(cards, h_type):
    test = cards
    number_of_Js = test.count("J")
        for card in CARDS:
            test.replace("J", card)

if __name__ == "__main__":
    main()
