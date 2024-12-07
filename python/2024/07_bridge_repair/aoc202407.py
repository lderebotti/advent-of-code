"""AoC 7, 2024: bridge_repair."""

# Standard library imports
import pathlib
import sys

import re
from itertools import product


def parse_data(puzzle_input):
    """Parse input."""
    # parse with regex
    return [
        (int(res), list(map(int, operators)))
        for res, *operators in (
            re.findall(r"\d+", line) for line in puzzle_input.splitlines()
        )
    ]


def part1(data):
    """Solve part 1."""
    add_mul = (lambda a, b: a + b, lambda a, b: a * b)
    total_calib = 0
    for line in data:
        res, operators = line
        for operations in product(add_mul, repeat=len(operators) - 1):
            solution = operators[0]
            for operator, operand in zip(operations, operators[1:]):
                solution = operator(solution, operand)
                if solution > res:
                    break
                if solution == res:
                    total_calib += res
                    break
            if solution == res:
                break

    return total_calib


def part2(data):
    """Solve part 2."""
    add_mul_conc = (
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: int(str(a) + str(b)),
    )
    total_calib = 0
    for line in data:
        res, operators = line
        for operations in product(add_mul_conc, repeat=len(operators) - 1):
            solution = operators[0]
            for operator, operand in zip(operations, operators[1:]):
                solution = operator(solution, operand)
                if solution > res:
                    break
                if solution == res:
                    total_calib += res
                    break
            if solution == res:
                break

    return total_calib


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
