from sys import argv, exit


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    histories = parse_file(argv[1])
    result = 0
    for history in histories:
        result += find_next_value(history)
    print(result)


def is_list_0(lst):
    return all(elem == 0 for elem in lst)


def find_next_value(history):
    sequences = []
    current = [int(nb) for nb in history.split()]
    while not is_list_0(current):
        sequences.append(current)
        current = [current[i + 1] - current[i] for i in range(len(current) - 1)]
    result = 0
    for seq in sequences[::-1]:
        result = seq[0] - result
    return result


def parse_file(path):
    with open(path, "r") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    main()
