from __future__ import annotations

import argparse
from pathlib import Path
from typing import Final

import elf

DEFAULT_YEAR: Final[int] = 2025
REPO_ROOT: Final[Path] = Path(__file__).resolve().parents[1]
SCRIPTS_DIR: Final[Path] = Path(__file__).resolve().parent
TEMPLATE_PATH: Final[Path] = SCRIPTS_DIR / "solution_template.py"


def render_template(day: int, year: int) -> str:
    """Render the shared template with the requested day and year."""
    text = TEMPLATE_PATH.read_text(encoding="utf-8")
    return text.format(DAY=day, YEAR=year)


def ensure_year_package(year: int) -> Path:
    """Ensure `<repo>/<year>/` exists and is a package."""
    year_dir = REPO_ROOT / str(year)
    year_dir.mkdir(exist_ok=True)

    init_file = year_dir / "__init__.py"
    if not init_file.exists():
        init_file.write_text(
            f'"""Advent of Code {year} solutions."""\n',
            encoding="utf-8",
        )
        print(f"📦 Initialized package {init_file}")

    return year_dir


def create_day(day: int, year: int) -> Path:
    """Create the dayXX skeleton for the given year."""
    if not 1 <= day <= 25:
        raise SystemExit("Day must be between 1 and 25.")

    if year < 2015:
        raise SystemExit("Advent of Code started in 2015; pick 2015 or later.")

    year_dir = ensure_year_package(year)
    day_dir = year_dir / f"day{day:02d}"
    day_dir.mkdir(exist_ok=True)

    solve_file = day_dir / "solve.py"
    if solve_file.exists():
        print(f"⚠️ {solve_file} already exists; not overwriting.")
        return solve_file

    solve_file.write_text(render_template(day, year), encoding="utf-8")
    print(f"✅ Created {solve_file}")

    # Create empty input files if they don't exist yet
    for name in ("input.txt", "test_input.txt"):
        path = day_dir / name
        if not path.exists():
            path.write_text("", encoding="utf-8")
    input_data = elf.get_puzzle_input(year, day)
    if input_data:
        input_path = day_dir / "input.txt"
        input_path.write_text(input_data, encoding="utf-8")
        print(f"✅ Wrote puzzle input to {input_path}")

    return solve_file


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create an Advent of Code solution stub.",
    )
    parser.add_argument(
        "day",
        type=int,
        help="Day number (1-25).",
    )
    parser.add_argument(
        "--year",
        "-y",
        type=int,
        default=DEFAULT_YEAR,
        help=f"Year to create (default: {DEFAULT_YEAR}).",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    print(f"🎄 Creating Advent of Code {args.year} — Day {args.day:02d}")
    create_day(args.day, args.year)


if __name__ == "__main__":
    main()
