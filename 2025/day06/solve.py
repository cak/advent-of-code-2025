from itertools import zip_longest
from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 06."""

DAY: int = 6
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 06."""
    homework_lines = [line.split() for line in data if line.strip()]
    homework_problems = [list(group) for group in zip(*homework_lines)]

    homework_total = 0
    for problem in homework_problems:
        sign = problem[-1]
        match sign:
            case "+":
                homework_total += sum(int(x) for x in problem[:-1])
            case "*":
                product = 1
                for x in problem[:-1]:
                    product *= int(x)
                homework_total += product
            case _:
                raise ValueError(f"Unknown sign: {sign}")

    return homework_total


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 06."""
    homework_problems = list(zip_longest(*data, fillvalue=" "))
    homework_total = 0

    current_problem = []
    all_problems = []
    for problem in homework_problems:
        list_problem = list(problem)
        if not [x for x in list_problem if x != " "]:
            all_problems.append(current_problem)
            current_problem = []
        else:
            current_problem.append(list_problem)
    if current_problem:
        all_problems.append(current_problem)

    for problem in all_problems:
        sign = problem[0][-1]
        problem[0][-1] = " "
        int_problem = [int("".join(row).strip()) for row in problem]
        total = 0
        match sign:
            case "+":
                total = sum(int_problem)
            case "*":
                product = 1
                for x in int_problem:
                    product *= x
                total = product
            case _:
                raise ValueError(f"Unknown sign: {sign}")
        homework_total += total

    return homework_total


def solve(part: Literal[1, 2], data: list[str]) -> int:
    """Dispatch to the appropriate part solution."""
    if part == 1:
        return part1(data)
    if part == 2:
        return part2(data)
    raise ValueError("part must be 1 or 2")


def main() -> None:
    """Main entry point."""
    input_file_name = "test_input.txt" if TEST else "input.txt"
    input_path = BASE_DIR / input_file_name

    raw_input = helpers.read_input(input_path)

    data_lines = helpers.parse_input(raw_input)

    print("🎄 Advent of Code 2025 - Day 06\n")

    result = solve(PART, data_lines)
    print("Part %d: %s\n" % (PART, result))

    if SUBMIT and not TEST:
        submit_result = submit_puzzle_answer(
            year=YEAR,
            day=DAY,
            part=PART,
            answer=str(result),
        )
        print(submit_result)


if __name__ == "__main__":
    main()
