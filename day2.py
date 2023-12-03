

number_of_cubes = {
    "red": 12, 
    "green": 13,
    "blue": 14
}


def part_one(lines: list):

    games = [line.split(":")[1].split(";") for line in lines]

    subsets = [list(map(lambda s: s.strip().split(","), game)) for game in games]
    
    n = 0
    possible = []
    for game in games:
        n += 1 
        subsets = list(map(lambda s: s.strip().split(","), game))

        is_possible = True
        for subset in subsets:
            for cube in subset:
                number = int(cube.split()[0].strip())
                color = cube.split()[1]
                if number > number_of_cubes[color]:
                    is_possible = False
                    break
        if is_possible: 
            possible.append(n)

    return sum(possible)


def main():
    with open("day2_input.txt") as f:
        lines = f.readlines()
        print(part_one(lines))

if __name__ == "__main__":
    main()