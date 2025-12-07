from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 07."""

DAY: int = 7
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 07."""
    diagram = [list(line) for line in data]
    start = diagram[0].index("S")
    indexes = [start]
    current_indexes = []
    splits = 0
    for r, row in enumerate(diagram[1:], start=1):
        for index in indexes:
            if index < 0 or index >= len(row):
                continue
            if row[index] == "^":
                splits += 1
                current_indexes.append(index - 1)
                current_indexes.append(index + 1)
            else:
                current_indexes.append(index)

        indexes = set(current_indexes)
        current_indexes = []

    return splits


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 07."""
    diagram = [list(line) for line in data]
    start = diagram[0].index("S")

    indexes_rows = {(0, start): 1}
    current_index_rows = {}
    for row in diagram[1:]:
        for r, index in indexes_rows:
            if index < 0 or index >= len(row):
                continue
            previous_count = indexes_rows.get((r, index), 0)

            if row[index] == "^":
                count_l = current_index_rows.get((r + 1, index - 1), 0)
                count_r = current_index_rows.get((r + 1, index + 1), 0)
                current_index_rows[(r + 1, index - 1)] = count_l + previous_count
                current_index_rows[(r + 1, index + 1)] = count_r + previous_count
            else:
                count = current_index_rows.get((r + 1, index), 0)
                current_index_rows[(r + 1, index)] = count + previous_count
        indexes_rows = current_index_rows
        current_index_rows = {}

    paths = sum(indexes_rows.values())

    return paths


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

    print("🎄 Advent of Code 2025 - Day 07\n")

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
