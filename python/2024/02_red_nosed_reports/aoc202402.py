"""AoC 2, 2024: red_nosed_reports."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [list(map(int, line.split())) for line in puzzle_input.splitlines()]


def is_sorted(line):
    for i in range(len(line) - 1):
        if line[i] > line[i + 1]:
            return False
    return True


def is_reverse_sorted(line):
    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            return False
    return True


def part1(data):
    """Solve part 1."""
    counter = 0
    for line in data:
        if is_sorted(line) or is_reverse_sorted(line):
            valid = True
            for i in range(len(line) - 1):
                diff = abs(line[i] - line[i + 1])
                if diff > 3 or diff < 1:
                    valid = False
                    break
            if valid:
                counter += 1
    return counter


def part2(data):
    """Solve part 2."""

    counter = 0
    for line in data:
        for i in range(len(line)):
            line_without_i = line[:i] + line[i + 1 :]
            if is_sorted(line_without_i) or is_reverse_sorted(line_without_i):
                valid = True
                for i in range(len(line_without_i) - 1):
                    diff = abs(line_without_i[i] - line_without_i[i + 1])
                    if diff > 3 or diff < 1:
                        valid = False
                        break
                if valid:
                    counter += 1
                    break

    return counter


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
