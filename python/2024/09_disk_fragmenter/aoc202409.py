"""AoC 9, 2024: disk_fragmenter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    state = "blocks"
    memory = []
    curr_id = 0
    for digit in puzzle_input:
        if state == "blocks":
            for _ in range(int(digit)):
                memory.append(str(curr_id))
            curr_id += 1
            state = "free"
            continue
        if state == "free":
            for _ in range(int(digit)):
                memory.append(".")
            state = "blocks"
            continue
    return memory


def part1(data):
    """Solve part 1."""
    memory_input = data.copy()
    free_space = memory_input.count(".")
    for _ in range(free_space):
        dot_index = memory_input.index(".")
        memory_input[dot_index], memory_input[-1] = (
            memory_input[-1],
            memory_input[dot_index],
        )
        memory_input.pop()

    filesystem_checksum = sum(
        [pos * int(block) for pos, block in enumerate(memory_input)]
    )
    return filesystem_checksum


def part2(data):
    """Solve part 2."""
    memory_input = data.copy()
    matches = []
    i = 0
    while i < len(memory_input):
        if memory_input[i] == ".":
            i += 1
            continue
        block = memory_input[i]
        start = i
        while i < len(memory_input) and memory_input[i] == block:
            i += 1
        matches.append((memory_input[start:i], start))

    matches = list(reversed(matches))

    for block, block_index in matches:
        block_size = len(block)
        free_space = []
        i = 0
        while i < len(memory_input) and i < block_index:
            if memory_input[i] == ".":
                start = i
                while i < len(memory_input) and memory_input[i] == ".":
                    i += 1
                free_space.append((start, memory_input[start:i]))
            else:
                i += 1

        for free_index, free_blocks in free_space:
            free_blocks_size = len(free_blocks)
            if free_blocks_size >= block_size and free_index < block_index:
                for i in range(block_size):
                    memory_input[free_index + i] = memory_input[block_index + i]
                    memory_input[block_index + i] = "."
                break

    filesystem_checksum = sum(
        [pos * int(block) for pos, block in enumerate(memory_input) if block != "."]
    )
    return filesystem_checksum


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
