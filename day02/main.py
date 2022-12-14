#!/usr/bin/python3

from pathlib import Path

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

games = [line.split() for line in content.splitlines()]
points = 0

# 'A' - 65 'B' - 66 'C' - 67 'X' - 88 'Y' - 89 'Z' - 90

def fight(p1, p2):
	p2 = p2 - 23
	if p1 == p2:
		return 3
	elif p1 > p2:
		if abs(p1 - p2) == 1:
			return 0
		else:
			return 6
	else:
		if abs(p1 - p2) == 1:
			return 6
		else:
			 return 0

for p1, p2 in games:
	p1 = ord(p1)
	p2 = ord(p2)
	points += p2 - 87
	points += fight(p1, p2)

print(f'Part 1: {points}')

points = 0
for p1, p2 in games:
	if p2 == 'X':
		if p1 == 'A':
			points += ord(p1) - 64 + 2
		else:
			points += ord(p1) - 64 - 1
	if p2 == 'Y':
		points += 3
		points += ord(p1) - 64
	if p2 == 'Z':
		points += 6
		if p1 == 'C':
			points += ord(p1) - 64 - 2
		else:
			points += ord(p1) - 64 + 1

print(f'Part 2: {points}')
