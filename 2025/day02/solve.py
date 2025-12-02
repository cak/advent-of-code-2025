from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 02."""

DAY: int = 2
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 02."""
    invalid_ids: list[int] = []
    for id in data:
        id_range = id.split("-")
        ids = list(range(int(id_range[0]), int(id_range[1]) + 1))
        for rid in ids:
            half = len(str(rid)) // 2
            first_half = str(rid)[:half]
            second_half = str(rid)[half:]
            if first_half == second_half:
                invalid_ids.append(rid)

    return sum(invalid_ids)


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 02."""
    invalid_ids: list[int] = []
    for id in data:
        id_range = id.split("-")
        ids = list(range(int(id_range[0]), int(id_range[1]) + 1))
        for rid in ids:
            str_rid = str(rid)
            for i in range(1, len(str_rid) + 1):
                first = str_rid[:i]
                second = str_rid[i : i + i]
                next = str_rid[i + i :]
                if first == second and (next == "" or next.replace(first, "") == ""):
                    invalid_ids.append(rid)
                    break

    return sum(invalid_ids)


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

    data_lines = raw_input.strip().split(",")

    print("🎄 Advent of Code 2025 - Day 02\n")

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
