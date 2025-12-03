from pathlib import Path
from typing import Literal

from elf import helpers, submit_puzzle_answer

"""Advent of Code 2025 - Day 03."""

DAY: int = 3
YEAR: int = 2025
BASE_DIR: Path = Path(__file__).parent

TEST: bool = True  # Set to False to use real input
PART: Literal[1, 2] = 2  # 1 or 2
SUBMIT: bool = True  # Set to True to submit the answer


def sort_digits_desc(n: int) -> int:
    return int("".join(sorted(str(n), reverse=True)))


@helpers.timer()
def part1(data: list[str]) -> int:
    """Solve Part 1 of Day 03."""

    banks = [[int(ch) for ch in data_line.strip()] for data_line in data]

    sorted_banks = [sorted(bank, reverse=True) for bank in banks]

    batteries: list[int] = []

    for bank, sorted_bank in zip(banks, sorted_banks):
        battery_one = (
            sorted_bank[0]
            if bank.index(sorted_bank[0]) != len(bank) - 1
            else sorted_bank[1]
        )

        banks_two = bank[bank.index(battery_one) + 1 :]
        sorted_banks_two = sorted(banks_two, reverse=True)
        battery_two = sorted_banks_two[0]
        batteries.append(int(f"{battery_one}{battery_two}"))

    return sum(batteries)


def find_larges_battery(bank: list[int], excluded_index: int) -> int:
    """Find the largest battery in the bank excluding the given index."""
    if len(bank) <= excluded_index - 1:
        return bank[0]

    safe_bank = bank[: excluded_index - 1]
    if not safe_bank:
        safe_bank = bank
    print(f"Safe bank (excluding index {excluded_index}): {safe_bank}")

    return sorted(safe_bank, reverse=True)[0]


@helpers.timer()
def part2(data: list[str]) -> int:
    """Solve Part 2 of Day 03."""

    banks = [[int(ch) for ch in data_line.strip()] for data_line in data]

    sorted_banks = [sorted(bank, reverse=True) for bank in banks]

    batteries: list[int] = []

    for bank, sorted_bank in zip(banks, sorted_banks):
        new_bank = bank
        bank_batteries: list[int] = []
        bank_range = min(12, len(new_bank))
        for i in range(bank_range):
            largest_battery = find_larges_battery(new_bank, bank_range - i)
            new_bank = new_bank[new_bank.index(largest_battery) + 1 :]
            if not new_bank:
                bank_batteries.append(largest_battery)
                break
            bank_batteries.append(largest_battery)
            print(f"Selected battery: {largest_battery}, Remaining bank: {new_bank}")

        print(bank_batteries)

    return sum(batteries)


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

    print("🎄 Advent of Code 2025 - Day 03\n")

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
