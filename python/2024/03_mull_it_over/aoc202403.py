"""AoC 3, 2024: mull_it_over."""

# Standard library imports
import pathlib
import sys
import re


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(data):
    """Solve part 1."""
    res = 0
    m = re.findall(r"mul\([0123456789]{1,3}\,[0123456789]{1,3}\)", data)
    for mul in m:
        op1 = re.search("\((.+?),", mul).group(1)
        op2 = re.search(",(.+?)\)", mul).group(1)
        res += int(op1) * int(op2)

    return res


def part2(data):
    """Solve part 2."""
    valid_mul_string = re.findall(r"mul\([0123456789]{1,3}\,[0123456789]{1,3}\)", data)
    valid_mul_positions = [
        x.start()
        for x in re.finditer(r"mul\([0123456789]{1,3}\,[0123456789]{1,3}\)", data)
    ]
    valid_mul = list(zip(valid_mul_positions, valid_mul_string))
    valid_do_string = re.findall(r"do\(\)", data)
    valid_do_positions = [x.start() for x in re.finditer(r"do\(\)", data)]
    valid_do = list(zip(valid_do_positions, valid_do_string))
    valid_dont_string = re.findall(r"don\'t\(\)", data)
    valid_dont_positions = [x.start() for x in re.finditer(r"don\'t\(\)", data)]
    valid_dont = list(zip(valid_dont_positions, valid_dont_string))
    valid = valid_mul + valid_do + valid_dont
    valid.sort()

    res = 0
    do_state = True
    for elem in valid:
        if elem[1] == "do()":
            do_state = True
        elif elem[1] == "don't()":
            do_state = False
        elif do_state and elem[1].find("u"):
            op1 = re.search("\((.+?),", elem[1]).group(1)
            op2 = re.search(",(.+?)\)", elem[1]).group(1)
            res += int(op1) * int(op2)

    return res


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
