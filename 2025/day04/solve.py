from itertools import product
from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 04."""

DAY: int = 4
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 04."""
    paper_grid = [list(line.strip()) for line in data]
    ROWS = len(paper_grid)
    COLS = len(paper_grid[0])

    rolls_assessable = 0

    for r, c in product(range(ROWS), range(COLS)):
        roll = paper_grid[r][c]
        if roll == ".":
            continue
        neighbors = []
        if c + 1 < COLS:
            neighbors.append(paper_grid[r][c + 1])
        if c - 1 >= 0:
            neighbors.append(paper_grid[r][c - 1])
        if r + 1 < ROWS:
            neighbors.append(paper_grid[r + 1][c])
        if r - 1 >= 0:
            neighbors.append(paper_grid[r - 1][c])
        if r + 1 < ROWS and c + 1 < COLS:
            neighbors.append(paper_grid[r + 1][c + 1])
        if r + 1 < ROWS and c - 1 >= 0:
            neighbors.append(paper_grid[r + 1][c - 1])
        if r - 1 >= 0 and c + 1 < COLS:
            neighbors.append(paper_grid[r - 1][c + 1])
        if r - 1 >= 0 and c - 1 >= 0:
            neighbors.append(paper_grid[r - 1][c - 1])

        if neighbors.count("@") < 4:
            rolls_assessable += 1

    return rolls_assessable


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 04."""
    paper_grid = [list(line.strip()) for line in data]
    ROWS = len(paper_grid)
    COLS = len(paper_grid[0])

    rolls_assessable = 0

    while True:
        rolls_to_remove = []

        for r, c in product(range(ROWS), range(COLS)):
            roll = paper_grid[r][c]
            if roll == ".":
                continue
            neighbors = []
            if c + 1 < COLS:
                neighbors.append(paper_grid[r][c + 1])
            if c - 1 >= 0:
                neighbors.append(paper_grid[r][c - 1])
            if r + 1 < ROWS:
                neighbors.append(paper_grid[r + 1][c])
            if r - 1 >= 0:
                neighbors.append(paper_grid[r - 1][c])
            if r + 1 < ROWS and c + 1 < COLS:
                neighbors.append(paper_grid[r + 1][c + 1])
            if r + 1 < ROWS and c - 1 >= 0:
                neighbors.append(paper_grid[r + 1][c - 1])
            if r - 1 >= 0 and c + 1 < COLS:
                neighbors.append(paper_grid[r - 1][c + 1])
            if r - 1 >= 0 and c - 1 >= 0:
                neighbors.append(paper_grid[r - 1][c - 1])

            if neighbors.count("@") < 4:
                rolls_assessable += 1
                rolls_to_remove.append((r, c))

        for r, c in rolls_to_remove:
            paper_grid[r][c] = "."

        if not rolls_to_remove:
            break

    return rolls_assessable


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

    print("🎄 Advent of Code 2025 - Day 04\n")

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
