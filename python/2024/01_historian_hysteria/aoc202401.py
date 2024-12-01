"""AoC 1, 2024: historian_hysteria."""

# Standard library imports
import pathlib
import sys
import numpy as np


def parse_data(puzzle_input):
    """Parse input."""
    return np.array(
        [list(map(int, line.split())) for line in puzzle_input.splitlines()]
    )


def part1(data):
    """Solve part 1."""
    first_list = data[:, 0]
    second_list = data[:, 1]

    return np.sum(np.abs(np.sort(first_list) - np.sort(second_list)))


def part2(data):
    """Solve part 2."""
    first_list = data[:, 0]
    second_list = data[:, 1]

    elements, counts = np.unique(second_list, return_counts=True)
    second_list_occurrences = dict(zip(elements, counts))

    return np.sum(
        np.array(
            [
                val * second_list_occurrences[val]
                for val in first_list
                if val in second_list_occurrences
            ]
        )
    )


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
