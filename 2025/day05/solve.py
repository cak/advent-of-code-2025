from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 05."""

DAY: int = 5
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = False  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


@helpers.timer()
def part1(data: str) -> int:
    """Solve Part 1 of Day 05."""
    data_id_ranges = data.split("\n\n")
    id_ranges_raw, ids = data_id_ranges[0], data_id_ranges[1]
    id_ranges = [x.split("-") for x in id_ranges_raw.splitlines() if x]

    available_fresh_ids = []

    for id in ids.splitlines():
        id_value = int(id)
        for id_range in id_ranges:
            start, end = int(id_range[0]), int(id_range[1]) + 1
            if id_value >= start and id_value <= end:
                available_fresh_ids.append(id_value)
                break

    return len(available_fresh_ids)


@helpers.timer()
def part2(data: str) -> int:
    """Solve Part 2 of Day 05."""
    data_id_ranges = data.split("\n\n")
    id_ranges_raw = data_id_ranges[0]
    id_ranges = [x.split("-") for x in id_ranges_raw.splitlines() if x]
    id_ranges = [(int(start), int(end)) for start, end in id_ranges]
    sorted_id_ranges = sorted(id_ranges, key=lambda x: x[0])
    fresh_ids = []

    for id_range in sorted_id_ranges:
        if not fresh_ids:
            fresh_ids.append(id_range)
            continue
        last_start, last_end = fresh_ids[-1]
        current_start, current_end = id_range
        if current_start <= last_end:
            fresh_ids[-1] = (last_start, max(last_end, current_end))
        else:
            fresh_ids.append(id_range)

    fresh_ids_count = sum(end - start + 1 for start, end in fresh_ids)

    return fresh_ids_count


def solve(part: Literal[1, 2], data: str) -> int:
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

    print("🎄 Advent of Code 2025 - Day 05\n")

    result = solve(PART, raw_input)
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
