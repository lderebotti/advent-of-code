"""AoC 5, 2024: print_queue."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    page_ordering_rules = [
        list(line.split("|"))
        for line in puzzle_input.splitlines()
        if line.find("|") != -1
    ]
    updates = [
        list(line.split(","))
        for line in puzzle_input.splitlines()
        if line and line.find("|") == -1
    ]
    return page_ordering_rules, updates


def part1(data):
    """Solve part 1."""
    page_ordering_rules, updates = data
    counter = 0

    for update in updates:
        to_print = True
        for page_ordering_rule in page_ordering_rules:
            first_elem, second_elem = page_ordering_rule
            if first_elem in update and second_elem in update:
                first_elem_idx = update.index(first_elem)
                second_elem_idx = update.index(second_elem)
                if first_elem_idx > second_elem_idx:
                    to_print = False
                    break
        if to_print:
            counter += int(update[len(update) // 2])

    return counter


def part2(data):
    """Solve part 2."""
    page_ordering_rules, updates = data
    counter = 0

    for update in updates:
        fixed = False
        to_print = False
        while not fixed:
            fixed = True
            for page_ordering_rule in page_ordering_rules:
                first_elem, second_elem = page_ordering_rule
                if first_elem in update and second_elem in update:
                    first_elem_idx = update.index(first_elem)
                    second_elem_idx = update.index(second_elem)
                    if first_elem_idx > second_elem_idx:
                        update[first_elem_idx], update[second_elem_idx] = (
                            update[second_elem_idx],
                            update[first_elem_idx],
                        )
                        to_print = True
                        fixed = False
                        break
        if to_print:
            counter += int(update[len(update) // 2])

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
