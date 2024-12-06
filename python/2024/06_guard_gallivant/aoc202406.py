"""AoC 6, 2024: guard_gallivant."""

# Standard library imports
import pathlib
import sys
import copy


def parse_data(puzzle_input):
    """Parse input."""
    data = puzzle_input.splitlines()
    curr_position = next(
        (
            [r, c]
            for r, row in enumerate(data)
            for c, char in enumerate(row)
            if char == "^"
        ),
        None,
    )
    if curr_position:
        curr_move = "UP"

    grid = [[False if char == "#" else True for char in row] for row in data]
    return grid, curr_position, curr_move


def move(grid, start_guard_position, start_move):
    curr_guard_position = start_guard_position.copy()
    curr_move = start_move
    visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    while True:
        if curr_move == "RIGHT":
            visited[curr_guard_position[0]][curr_guard_position[1]] = True
            if curr_guard_position[1] + 1 >= len(grid[0]):
                return visited
            if grid[curr_guard_position[0]][curr_guard_position[1] + 1]:
                curr_guard_position[1] += 1
            else:
                curr_move = "DOWN"
        elif curr_move == "DOWN":
            visited[curr_guard_position[0]][curr_guard_position[1]] = True
            if curr_guard_position[0] + 1 >= len(grid):
                return visited
            if grid[curr_guard_position[0] + 1][curr_guard_position[1]]:
                curr_guard_position[0] += 1
            else:
                curr_move = "LEFT"
        elif curr_move == "LEFT":
            visited[curr_guard_position[0]][curr_guard_position[1]] = True
            if curr_guard_position[1] - 1 < 0:
                return visited
            if grid[curr_guard_position[0]][curr_guard_position[1] - 1]:
                curr_guard_position[1] -= 1
            else:
                curr_move = "UP"
        elif curr_move == "UP":
            visited[curr_guard_position[0]][curr_guard_position[1]] = True
            if curr_guard_position[0] - 1 < 0:
                return visited
            if grid[curr_guard_position[0] - 1][curr_guard_position[1]]:
                curr_guard_position[0] -= 1
            else:
                curr_move = "RIGHT"


def part1(data):
    """Solve part 1."""
    grid, curr_position, curr_move = data
    visited = move(grid, curr_position, curr_move)
    return sum(sum(row) for row in visited)


def check_loop(grid, start_guard_position, start_move):
    curr_guard_position = start_guard_position.copy()
    curr_move = start_move
    visited_states = set()
    while True:
        state = (curr_guard_position[0], curr_guard_position[1], curr_move)
        if state in visited_states:
            return True
        visited_states.add(state)
        if curr_move == "RIGHT":
            if curr_guard_position[1] + 1 >= len(grid[0]):
                return False
            if grid[curr_guard_position[0]][curr_guard_position[1] + 1]:
                curr_guard_position[1] += 1
            else:
                curr_move = "DOWN"
        elif curr_move == "DOWN":
            if curr_guard_position[0] + 1 >= len(grid):
                return False
            if grid[curr_guard_position[0] + 1][curr_guard_position[1]]:
                curr_guard_position[0] += 1
            else:
                curr_move = "LEFT"
        elif curr_move == "LEFT":
            if curr_guard_position[1] - 1 < 0:
                return False
            if grid[curr_guard_position[0]][curr_guard_position[1] - 1]:
                curr_guard_position[1] -= 1
            else:
                curr_move = "UP"
        elif curr_move == "UP":
            if curr_guard_position[0] - 1 < 0:
                return False
            if grid[curr_guard_position[0] - 1][curr_guard_position[1]]:
                curr_guard_position[0] -= 1
            else:
                curr_move = "RIGHT"


def part2(data):
    """Solve part 2."""
    counter = 0
    grid, start_guard_position, start_move = data
    visited = move(grid, start_guard_position, start_move)
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] and visited[r][c] and [r, c] != start_guard_position:
                test_grid = copy.deepcopy(grid)
                test_curr_position = start_guard_position.copy()
                test_curr_move = start_move
                test_grid[r][c] = False
                if check_loop(test_grid, test_curr_position, test_curr_move):
                    counter += 1
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
