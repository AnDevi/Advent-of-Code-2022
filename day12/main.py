#!/usr/bin/python3

from pathlib import Path

dir_x = [1, -1,  0,  0]
dir_y = [0,  0,  1, -1]

def grid_print(grid):
	w, h = len(grid[0]), len(grid)
	for y in range(h):
		print(''.join([str(grid[y][x]) for x in range(w)]))
	print()

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()
grid = [[c for c in line.strip()] for line in content.splitlines()]

def find_shortest_path(grid, sx, sy):
    w, h = len(grid[0]), len(grid)
    visited = [[0 for _ in range(w)] for _ in range(h)]
    queue = []
    queue.append((sx, sy))

    while len(queue) != 0:
        x, y = queue.pop(0)
        height = grid[y][x] if grid[y][x] != 'S' else 'a'
        for dx, dy in zip(dir_x, dir_y):
            cx, cy = x + dx, y + dy
            if cx < 0 or cy < 0 or cx >= w or cy >= h:
                continue
            if grid[cy][cx] == 'E' and (grid[y][x] == 'y' or grid[y][x] == 'z'):
                return visited[y][x] + 1
            if visited[cy][cx] > 0:
                continue
            curr_height = grid[cy][cx]
            if ord(curr_height) - ord(height) <= 1:
                queue.append((cx, cy))
                visited[cy][cx] = visited[y][x] + 1

sx, sy = 0, 0
w, h = len(grid[0]), len(grid)
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'S':
            sx, sy = x, y
shortest_path = find_shortest_path(grid, sx, sy)
print(f'Part 1: {shortest_path}')

path_lengths = list()
path_lengths.append(shortest_path)
poss_start = list()
for y in range(h):
    for x in range(w):
        if grid[y][x] == 'a':
            poss_start.append((x, y))

grid[sy][sx] = 'a'
for x, y in poss_start:
    shortest_path = find_shortest_path(grid, x, y)
    if shortest_path:
        path_lengths.append(shortest_path)

print(f'Part 2: {min(path_lengths)}')
