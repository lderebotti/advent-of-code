"""AoC 7, 2024: bridge_repair."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return list(
        [elem.strip(":") for elem in line.split()] for line in puzzle_input.splitlines()
    )


def evaluate_left_to_right_binary(expr):
    tokens = []
    num = ""
    for c in expr:
        if c in "+*":
            tokens.append(int(num))
            tokens.append(c)
            num = ""
        else:
            num += c
    tokens.append(int(num))
    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_num = tokens[i + 1]
        if op == "+":
            result += next_num
        elif op == "*":
            result *= next_num
        i += 2
    return result


def part1(data):
    """Solve part 1."""
    accumulator = 0
    for line in data:
        result = int(line[0])

        operators = []
        for i in range((len(line) - 2)):
            operators.append(["+", "*"])

        for i in range(2 ** (len(line) - 2)):
            binary = format(i, f"0{len(line) - 2}b")
            expression = line[1]
            for j in range(len(binary)):
                expression += operators[j][int(binary[j])] + line[j + 2]
            test_result = evaluate_left_to_right_binary(expression)
            if test_result == result:
                accumulator += test_result
                break
    return accumulator


def convert_to_base(n, base, length):
    digits = []
    while n > 0:
        digits.append(str(n % base))
        n //= base
    while len(digits) < length:
        digits.append("0")
    return "".join(reversed(digits))


def evaluate_left_to_right_ternary(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i : i + 2] == "||":
            tokens.append("||")
            i += 2
        elif expr[i] in "+*":
            tokens.append(expr[i])
            i += 1
        elif expr[i].isdigit():
            num = ""
            while i < len(expr) and expr[i].isdigit():
                num += expr[i]
                i += 1
            tokens.append(int(num))
        else:
            i += 1  # Skip unknown characters
    result = tokens[0]
    i = 1
    while i < len(tokens):
        op = tokens[i]
        next_num = tokens[i + 1]
        if op == "+":
            result += next_num
        elif op == "*":
            result *= next_num
        elif op == "||":
            result = int(str(result) + str(next_num))
        i += 2
    return result


def part2(data):
    """Solve part 2."""
    # TODO: implement DFS
    accumulator = 0
    for line in data:
        result = int(line[0])

        operators = []
        for i in range((len(line) - 2)):
            operators.append(["+", "*", "||"])

        for i in range(3 ** (len(line) - 2)):
            ternary = convert_to_base(i, 3, len(line) - 2)
            expression = line[1]
            for j in range(len(ternary)):
                expression += operators[j][int(ternary[j])] + line[j + 2]
            evaluated_result = evaluate_left_to_right_ternary(expression)
            if evaluated_result == result:
                accumulator += evaluated_result
                break

    return accumulator


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
