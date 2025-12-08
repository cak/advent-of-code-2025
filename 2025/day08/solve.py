import math
from pathlib import Path
from queue import PriorityQueue
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 08."""

DAY: int = 8
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = True  # Set to False to use real input
PART: Literal[1, 2] = 1  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 08."""
    c_split = [line.split(",") for line in data]
    coordinates = [(int(x), int(y), int(z)) for x, y, z in c_split]

    results = PriorityQueue(1000)
    for x1, y1, z1 in coordinates:
        min_distance = results.queue[0][0] if not results.empty() else 0.0
        for x2, y2, z2 in coordinates:
            if ((x2, y2, z2), (x1, y1, z1)) in results.queue:
                continue

            if (x1, y1, z1) == (x2, y2, z2):
                continue
            distance = math.dist((x1, y1, z1), (x2, y2, z2))
            if (
                (distance < min_distance)
                or (min_distance == 0.0)
                or results.qsize() <= 1000
            ):
                results.put((distance, ((x1, y1, z1), (x2, y2, z2))))
    print(results)

    return len(data)


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 08."""
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

    raw_input = helpers.read_input(input_path)

    data_lines = helpers.parse_input(raw_input)

    print("🎄 Advent of Code 2025 - Day 08\n")

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
