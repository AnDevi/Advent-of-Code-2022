#!/usr/bin/python3

from pathlib import Path
import copy
import re

TEST = {
	1 : ['Z', 'N'],
	2 : ['M', 'C', 'D'],
	3 : ['P'],
}

PART = {
	1 : ['P', 'F', 'M', 'Q', 'W', 'G', 'R', 'T'],
	2 : ['H', 'F', 'R'],
	3 : ['P', 'Z', 'R', 'V', 'G', 'H', 'S', 'D'],
	4 : ['Q', 'H', 'P', 'B', 'F', 'W', 'G'],
	5 : ['P', 'S', 'M', 'J', 'H'],
	6 : ['M', 'Z', 'T', 'H', 'S', 'R', 'P', 'L'],
	7 : ['P', 'T', 'H', 'N', 'M', 'L'], 
	8 : ['F', 'D', 'Q', 'R'],
	9 : ['D', 'S', 'C', 'N', 'L', 'P', 'H']
}

def print_dict(dict):
	for key in dict:
		line = str(key) + ' '	
		for c in dict[key]:
			line += f"'{c}'" + ' '
		print(line)
	print()

def move(cargo, moves, is_CrateMover_9001 = False):
	
	for move in moves:
		cnt, start, end = move[0], move[1], move[2]
		for i in range(cnt):
			if is_CrateMover_9001: 
				cargo[end].append(cargo[start][-(cnt - i)])
			else:
				cargo[end].append(cargo[start][-1])
				cargo[start].pop()
		if is_CrateMover_9001:
			cargo[start] = cargo[start][:len(cargo[start]) - cnt]
		print_dict(cargo)	

	result = str()
	for key in cargo:
		result += cargo[key][-1]

	return result

content = Path(Path(__file__).parent.resolve() / 'day5.txt').read_text()

LOG_RE = re.compile(r"move (\d+) from (\d+) to (\d+)")

moves = []
for line in content.splitlines():
	m = re.match(LOG_RE, line)
	moves.append((int(m.group(1)), int(m.group(2)), int(m.group(3))))


cargo = copy.deepcopy(PART)
result = move(cargo, moves)

print(f'Part 1: {result}')

cargo = copy.deepcopy(PART)
result = move(cargo, moves, is_CrateMover_9001=True)

print(f'Part 2: {result}')
