#!/usr/bin/python3

from pathlib import Path
import numpy

dir_x = [1, -1,  0,  0]
dir_y = [0,  0,  1, -1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

grid = [[int(num) for num in line.strip()] for line in content.splitlines()]
# grid_print(grid)

visables = 0
w, h = len(grid[0]), len(grid)

# add egdes
visables += 2 * w +  2 * h - 4

# add center
for y in range(1, h - 1):
    for x in range(1, w - 1):
        tree = grid[y][x]
        visable = False
        for dx, dy in zip(dir_x, dir_y):
            if not visable:
                for r in range(1, w - 1):
                    cx, cy = x + dx * r, y + dy * r
                    if cx < 0 or cy < 0 or cx >= w or cy >= h:
                        break
                    if tree <= grid[cy][cx]:
                        visable = False
                        break
                    visable = True
        if visable:
            visables += 1

print(f'Part 1: {visables}')

all_scenics = []
for y in range(1, h - 1):
    for x in range(1, w - 1):
        tree = grid[y][x]
        scenic = []
        for dx, dy in zip(dir_x, dir_y):
            trees = 0
            for r in range(1, w - 1):
                cx, cy = x + dx * r, y + dy * r
                if cx < 0 or cy < 0 or cx >= w or cy >= h:
                    break
                if tree > grid[cy][cx]:
                    trees += 1
                else:
                    trees += 1
                    break
            scenic.append(trees)
        all_scenics.append(numpy.prod(scenic))

print(f'Part 2: {max(all_scenics)}')
