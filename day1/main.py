#!/usr/bin/python3

from pathlib import Path

content = Path(Path(__file__).parent.resolve() / 'day1.txt').read_text()

elfs_str = content.split("\n\n")
elfs = []

for elf in elfs_str:
	elfs.append(list(map(int, elf.splitlines())))

elfs_calories = []

for elf in elfs:
	elfs_calories.append(sum(elf))

print(f'Part 1: {max(elfs_calories)}')

last_three = sum(sorted(elfs_calories)[-3:])

print(f'Part 2: {last_three}')
				