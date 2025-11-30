# advent-of-code-2025

These are my personal Advent of Code 2025 solutions, built as a way to practice problem-solving, explore implementation ideas, and have fun during the holiday season. 🎄

The repository uses my Python package [`elf`](https://github.com/cak/elf) to fetch inputs, time solutions, and submit answers safely. Each day’s solution is self-contained, reproducible, and generated from a simple template for quickly getting started.

This repo is structured for **2025 only**.

---

## Requirements

You **must install `elf`** before running or generating any solution files:

```bash
uv tool install elf    # recommended
# or:
pip install elf
```

Your Advent of Code `session` cookie must be available via the `AOC_SESSION` environment variable for input fetching and submissions.

---

## Layout

```
2025/
  dayXX/
    solve.py           # template-based solution file
    input.txt          # your personal puzzle input (never commit)
    test_input.txt     # example/sample input for testing
scripts/
  new_day.py           # scaffolds new days and input boilerplate
  solution_template.py # template used to generate a new day
```

- Each day lives in its own folder: `2025/day01/`, `2025/day02/`, etc.
- `solve.py` includes toggles for `TEST`, `PART`, and `SUBMIT`.
- Inputs are stored locally per day so repeated runs do not hit AoC servers.

---

## Getting Started

1. Install project dependencies (if you're using `uv` with a lockfile):

   ```bash
   uv sync --upgrade
   ```

2. Run any day:

   ```bash
   python 2025/day01/solve.py            # use your real input
   ```

3. Run with test input:

   ```bash
   TEST=true python 2025/day01/solve.py  # or toggle TEST inside the file
   ```

The solutions rely on `elf.helpers` for parsing, timing, and submission support.  
If `AOC_SESSION` is missing, input fetches and submissions will fail cleanly.

---

## Adding a New Day

Use the helper script instead of copying files manually:

```bash
python scripts/new_day.py <day> [--year YEAR]
```

This will:

- Create the directory (`2025/dayXX/` or the requested year)
- Generate `solve.py` from `scripts/solution_template.py`
- Create empty `input.txt` and `test_input.txt`
- Ensure the year directory exists (no package unless you add one manually)
- (Optional) Easily extend to auto-fetch input via `elf`

After scaffolding:

1. Open the new day's `solve.py`
2. Implement `part1` and `part2`
3. Test with sample input
4. Switch `TEST=False` and run again with real input
5. Set `SUBMIT=True` to safely send the answer using `elf`

---

## Tips

- **Never commit your real input files** (`input.txt` is personal).
- Use `test_input.txt` for experimenting, verifying parsing, and iterating quickly.
- If you adjust the structure of your solutions, update `scripts/solution_template.py` and regenerate as needed.
- Each solution file is self-contained: toggle `TEST`, `PART`, and `SUBMIT` directly in the script.

---

Happy coding, and good luck with Advent of Code 2025! 🎄
