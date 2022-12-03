#!/usr/bin/python3

from pathlib import Path

content = Path(Path(__file__).parent.resolve() / 'day3.txt').read_text()

def priority(c):
	return ord(c) - ord('A') + 27 if c.isupper() else ord(c) - ord('a') + 1

packs = [list(line) for line in content.splitlines()]
priority_sum = 0
for pack in packs:
	commons = set(pack[:len(pack) // 2]) & set(pack[len(pack) // 2:])
	for c in commons:
		priority_sum += priority(c)
	
print(f'Part 1: {priority_sum}')

priority_sum = 0
groups = [packs[i:i+3] for i in range(0, len(packs), 3)]
for g in groups:
	commons = set(g[0]) & set(g[1]) & set(g[2])
	for c in commons:
		priority_sum += priority(c)

print(f'Part 2: {priority_sum}')
