"""AoC 4, 2024: ceres_search."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    num_rows = len(data)
    num_cols = len(data[0])
    count = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if data[r][c] == "X":
                if r >= 3:
                    if (
                        data[r - 1][c] == "M"
                        and data[r - 2][c] == "A"
                        and data[r - 3][c] == "S"
                    ):
                        count += 1
                if c >= 3:
                    if (
                        data[r][c - 1] == "M"
                        and data[r][c - 2] == "A"
                        and data[r][c - 3] == "S"
                    ):
                        count += 1
                if r >= 3 and c >= 3:
                    if (
                        data[r - 1][c - 1] == "M"
                        and data[r - 2][c - 2] == "A"
                        and data[r - 3][c - 3] == "S"
                    ):
                        count += 1
                if r <= num_rows - 4:
                    if (
                        data[r + 1][c] == "M"
                        and data[r + 2][c] == "A"
                        and data[r + 3][c] == "S"
                    ):
                        count += 1
                if c <= num_cols - 4:
                    if (
                        data[r][c + 1] == "M"
                        and data[r][c + 2] == "A"
                        and data[r][c + 3] == "S"
                    ):
                        count += 1
                if r <= num_rows - 4 and c <= num_cols - 4:
                    if (
                        data[r + 1][c + 1] == "M"
                        and data[r + 2][c + 2] == "A"
                        and data[r + 3][c + 3] == "S"
                    ):
                        count += 1
                if r <= num_rows - 4 and c >= 3:
                    if (
                        data[r + 1][c - 1] == "M"
                        and data[r + 2][c - 2] == "A"
                        and data[r + 3][c - 3] == "S"
                    ):
                        count += 1
                if r >= 3 and c <= num_cols - 4:
                    if (
                        data[r - 1][c + 1] == "M"
                        and data[r - 2][c + 2] == "A"
                        and data[r - 3][c + 3] == "S"
                    ):
                        count += 1

    return count


def part2(data):
    """Solve part 2."""

    num_rows = len(data)
    num_cols = len(data[0])
    count = 0
    for r in range(1, num_rows - 1):
        for c in range(1, num_cols - 1):
            if data[r][c] == "A":
                if (
                    data[r - 1][c - 1] == data[r + 1][c - 1] == "M"
                    and data[r - 1][c + 1] == data[r + 1][c + 1] == "S"
                ):
                    count += 1
                if (
                    data[r - 1][c - 1] == data[r + 1][c - 1] == "S"
                    and data[r - 1][c + 1] == data[r + 1][c + 1] == "M"
                ):
                    count += 1
                if (
                    data[r - 1][c - 1] == data[r - 1][c + 1] == "M"
                    and data[r + 1][c - 1] == data[r + 1][c + 1] == "S"
                ):
                    count += 1
                if (data[r - 1][c - 1] == data[r - 1][c + 1] == "S") and (
                    data[r + 1][c - 1] == data[r + 1][c + 1] == "M"
                ):
                    count += 1

    return count


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
