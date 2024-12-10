"""AoC 10, 2024: hoof_it."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.splitlines()]


def move(curr_value, r, c, data, peaks_found, visited):
    if data[r][c] == "9":
        if (r, c) in visited:
            return
        visited.add((r, c))
        peaks_found[0] += 1
        return
    if c + 1 < len(data[0]) and int(data[r][c + 1]) == curr_value + 1:
        move(curr_value + 1, r, c + 1, data, peaks_found, visited)
    if r + 1 < len(data) and int(data[r + 1][c]) == curr_value + 1:
        move(curr_value + 1, r + 1, c, data, peaks_found, visited)
    if c - 1 >= 0 and int(data[r][c - 1]) == curr_value + 1:
        move(curr_value + 1, r, c - 1, data, peaks_found, visited)
    if r - 1 >= 0 and int(data[r - 1][c]) == curr_value + 1:
        move(curr_value + 1, r - 1, c, data, peaks_found, visited)


def part1(data):
    """Solve part 1."""
    peaks_found = [0]
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "0":
                visited = set()
                move(0, r, c, data, peaks_found, visited)

    return peaks_found[0]


def move_part2(curr_value, r, c, data, peaks_found):
    if data[r][c] == "9":
        peaks_found[0] += 1
        return
    if c + 1 < len(data[0]) and int(data[r][c + 1]) == curr_value + 1:
        move_part2(curr_value + 1, r, c + 1, data, peaks_found)
    if r + 1 < len(data) and int(data[r + 1][c]) == curr_value + 1:
        move_part2(curr_value + 1, r + 1, c, data, peaks_found)
    if c - 1 >= 0 and int(data[r][c - 1]) == curr_value + 1:
        move_part2(curr_value + 1, r, c - 1, data, peaks_found)
    if r - 1 >= 0 and int(data[r - 1][c]) == curr_value + 1:
        move_part2(curr_value + 1, r - 1, c, data, peaks_found)


def part2(data):
    """Solve part 2."""
    peaks_found = [0]
    for r in range(len(data)):
        for c in range(len(data[0])):
            if data[r][c] == "0":
                move_part2(0, r, c, data, peaks_found)

    return peaks_found[0]


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
