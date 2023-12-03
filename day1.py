import re

def part_one(lines : list):

    numbers = [re.findall(r'(\d)', line) for line in lines]
    combines = [int("".join([num[0] + num[-1]])) for num in numbers] 

    return sum(combines)


def part_two(lines : list):
    literals = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    regex_numbers = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))'

    numbers = [list(map(lambda n: literals.index(n) + 1 if len(n) > 1 else int(n), re.findall(regex_numbers, line))) for line in lines]
    combines = [int("".join([str(num[0]) + str(num[-1])])) for num in numbers]

    return sum(combines)


def main():
    input = open('day1_input.txt').readlines()
    print("Day 1 p1: ", part_one(input))
    print("Day 1 p2: ", part_two(input))


if __name__ == '__main__':
    main()