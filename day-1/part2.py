from sys import argv, exit

NUMBERS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


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
        for i, char in enumerate(line):
            if char.isdigit():
                digits += char
            index = is_a_digit_word(line, i)
            if index != -1:
                digits += convert_letter_to_dig(index)
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


def is_a_digit_word(line, index):
    line = line[index:]
    for i, number in enumerate(NUMBERS):
        if matches(line, number, len(number)):
            return i
    return -1


def convert_letter_to_dig(index):
    return str(index + 1)


def matches(s1, s2, size):
    return s1[:size] == s2[:size]


main()
