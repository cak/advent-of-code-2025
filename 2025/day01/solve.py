from __future__ import annotations

from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 01."""

DAY: int = 1
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


def rotate_safe(
    direction: str, value: str, starting_value: int = 50, modulus: int = 100
) -> int:
    """Rotate the facing direction safely."""

    match direction:
        case "R":
            return (starting_value + int(value)) % modulus
        case "L":
            return (starting_value - int(value)) % modulus
    raise ValueError("direction must be 'R' or 'L'")


def rotate_safe_two(
    direction: str, value: str, starting_value: int = 50, modulus: int = 100
) -> tuple[int, int]:
    """Rotate the facing direction safely."""
    ending_value = 0
    zeros = 0
    match direction:
        case "R":
            ending_value = starting_value + int(value)
        case "L":
            ending_value = starting_value - int(value)

    for i in range(starting_value, ending_value, 1 if direction == "R" else -1):
        if i % modulus == 0:
            zeros += 1

    return (ending_value, zeros)


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 01."""

    rotations = [(line[0:1], line[1:]) for line in data]

    anwser = 0
    result = 50
    for direction, value in rotations:
        result = rotate_safe(direction, value, result)
        if result == 0:
            anwser += 1

    return anwser


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 01."""
    rotations = [(line[0:1], line[1:]) for line in data]

    zero_total = 0
    result = 50
    for direction, value in rotations:
        result, zeros = rotate_safe_two(direction, value, result)
        zero_total += zeros

    return zero_total


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

    print(input_path)

    with open(input_path, "r", encoding="utf-8") as f:
        raw_input = f.read()

    data_lines = helpers.parse_input(raw_input)

    print("🎄 Advent of Code 2025 - Day 01\n")

    result = solve(PART, data_lines)
    print("Part %d: %s\n" % (PART, result))

    if SUBMIT and not TEST:
        submit = submit_puzzle_answer(
            year=YEAR,
            day=DAY,
            part=PART,
            answer=str(result),
        )
        print(submit)


if __name__ == "__main__":
    main()
