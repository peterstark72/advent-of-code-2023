import re

def part_one(lines : list):

    numbers = [re.findall(r'(\d)', line) for line in lines]
    combines = [int("".join([num[0] + num[-1]])) for num in numbers] 

    return sum(combines)


def main():
    input = open('day1_input.txt').readlines()
    print(part_one(input))


if __name__ == '__main__':
    main()