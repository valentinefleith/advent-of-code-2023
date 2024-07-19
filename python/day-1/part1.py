from sys import argv, exit


def main():
    if len(argv) != 2:
        exit("Il faut un fichier en argument.")
    lines = get_file_lines(argv[1])
    digits = get_numbers(lines)
    two_digits = get_two_digits(digits)
    total = sum(two_digits)
    print(total)


def get_file_lines(path):
    with open(path, "r") as file:
        return file.readlines()


def get_numbers(lines):
    numbers = []
    for line in lines:
        digits = ""
        for char in line:
            if char.isdigit():
                digits += char
        if digits:
            numbers.append(digits)
    return numbers


def get_two_digits(digits):
    two = []
    for digit in digits:
        if len(digit) > 2:
            two.append(f"{digit[0]}{digit[-1]}")
        elif len(digit) == 1:
            two.append(f"{digit}{digit}")
        else:
            two.append(digit)
    return [int(dig) for dig in two]


main()
