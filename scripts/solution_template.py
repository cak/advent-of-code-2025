from __future__ import annotations

from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code {YEAR} - Day {DAY:02d}."""

DAY: int = {DAY}
YEAR: int = {YEAR}
BASE_DIR: Path = Path(__file__).parent

TEST: bool = True  # Set to False to use real input
PART: Literal[1, 2] = 1  # 1 or 2
SUBMIT: bool = False  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day {DAY:02d}."""
    # TODO: implement Part 1
    return len(data)


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day {DAY:02d}."""
    # TODO: implement Part 2
    return len(data)


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

    raw_input = helpers.read_test_input(input_path)
    data_lines = helpers.parse_input(raw_input)

    print(f"🎄 Advent of Code {YEAR} - Day {DAY:02d}\n")

    result = solve(PART, data_lines)
    print("Part %d: %s\n" % (PART, result))

    if SUBMIT and not TEST:
        submit_puzzle_answer(
            year=YEAR,
            day=DAY,
            part=PART,
            answer=str(result),
        )


if __name__ == "__main__":
    main()
