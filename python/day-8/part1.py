from sys import argv, exit


def main():
    if len(argv) != 2:
        exit("Il faut l'input en argument.")
    instructions, nodes = parse_file(argv[1])
    steps = count_steps_to_end(instructions, nodes)
    print(steps)


class Node:
    def __init__(self, current, right, left):
        self.current = current
        self.right = right
        self.left = left


def count_steps_to_end(instructions, nodes):
    count = 0
    current_elem = "AAA"
    while current_elem != "ZZZ":
        for letter in instructions:
            current_node = nodes[find_index_of_elem(current_elem, nodes)]
            current_elem = current_node.right if letter == "R" else current_node.left
            count += 1
            if current_elem == "ZZZ":
                break
    return count


def find_index_of_elem(current_elem, nodes):
    for i, node in enumerate(nodes):
        if node.current == current_elem:
            return i
    return -1


def parse_file(path):
    with open(path, "r") as file:
        instructions = file.readline().strip()
        steps = []
        for line in file.readlines()[1:]:
            current = line.split()[0]
            right = line.split("=")[1].split(",")[1][:-2].strip()
            left = line.split("=")[1].split(",")[0][2:].strip()
            steps.append(Node(current, right, left))
        return instructions, steps


if __name__ == "__main__":
    main()
