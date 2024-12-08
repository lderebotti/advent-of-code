"""AoC 8, 2024: resonant_collinearity."""

# Standard library imports
import pathlib
import sys
from itertools import product
import numpy as np


def parse_data(puzzle_input):
    """Parse input."""
    return [list(line) for line in puzzle_input.splitlines()]


def part1(data):
    """Solve part 1."""
    grid_size = len(data), len(data[0])
    antennas = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((x, y))
    for char, coords in antennas.items():
        antennas[char] = list(product(coords, repeat=2))

    antinode_locations = [[False] * grid_size[1] for _ in range(grid_size[0])]
    for _, coords in antennas.items():
        for (x1, y1), (x2, y2) in coords:
            if (x1 == x2) and (y1 == y2):
                continue
            dist12_x = x1 - x2
            dist12_y = y1 - y2
            dist21_x = x2 - x1
            dist21_y = y2 - y1
            if (
                x1 + dist12_x >= 0
                and x1 + dist12_x < grid_size[1]
                and y1 + dist12_y >= 0
                and y1 + dist12_y < grid_size[0]
            ):
                antinode_locations[x1 + dist12_x][y1 + dist12_y] = True
            if (
                x2 + dist21_x >= 0
                and x2 + dist21_x < grid_size[1]
                and y2 + dist21_y >= 0
                and y2 + dist21_y < grid_size[0]
            ):
                antinode_locations[x2 + dist21_x][y2 + dist21_y] = True

    return np.count_nonzero(antinode_locations)


def part2(data):
    """Solve part 2."""
    grid_size = len(data), len(data[0])
    antennas = {}
    for y, line in enumerate(data):
        for x, char in enumerate(line):
            if char != ".":
                antennas.setdefault(char, []).append((x, y))
    for char, coords in antennas.items():
        antennas[char] = list(product(coords, repeat=2))

    antinode_locations = [[False] * grid_size[1] for _ in range(grid_size[0])]
    for _, coords in antennas.items():
        for (x1, y1), (x2, y2) in coords:
            if (x1 == x2) and (y1 == y2):
                continue
            dist12_x = x1 - x2
            dist12_y = y1 - y2
            x = x1
            y = y1
            while x >= 0 and x < grid_size[1] and y >= 0 and y < grid_size[0]:
                antinode_locations[x][y] = True
                x += dist12_x
                y += dist12_y

    return np.count_nonzero(antinode_locations)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    # yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
