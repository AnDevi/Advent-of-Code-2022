#!/usr/bin/python3

from pathlib import Path

dir_x = [1, -1,  0,  0,  1, 1, -1, -1]
dir_y = [0,  0,  1, -1, -1, 1,  1, -1]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f'Point x {self.x} y {self.y}'
    def __repr__(self):
        return f'Point x={self.x} y={self.y}'
    def __eq__(self, other):
        return (isinstance(other, self.__class__) and
            getattr(other, 'x', None) == self.x and
            getattr(other, 'y', None) == self.y)


def should_t_move(t_pos, h_pos):
    if h_pos== t_pos:
        return False
    for x, y in zip(dir_x, dir_y):
        cx, cy = t_pos.x + x, t_pos.y + y
        if cx == h_pos.x and cy == h_pos.y:
            return False
    return True

def move_knots(moves, knots_cnt):
    last_knot_positions = set()
    h_pos = Point(0, 0)
    knots_pos = []
    for _ in range(knots_cnt):
        knots_pos.append(Point(0,0))
    last_knot_positions.add((knots_pos[-1].x, knots_pos[-1].y))

    for move in moves:
        if move == 'R':
            h_pos.x += 1
        elif move == 'L':
            h_pos.x -= 1
        elif move == 'U':
            h_pos.y -= 1
        elif move == 'D':
            h_pos.y += 1

        for i in range(len(knots_pos)):
            if i == 0:
                first, second = knots_pos[i], h_pos
            else:
                first, second = knots_pos[i], knots_pos[i - 1]

            if should_t_move(first, second):            
                diff_x = second.x - first.x
                diff_y = second.y - first.y
                if diff_x != 0:
                    first.x += diff_x // 2 if diff_x % 2 == 0 else diff_x
                if diff_y != 0:
                    first.y += diff_y // 2 if diff_y % 2 == 0 else diff_y
        
        last_knot_positions.add((knots_pos[-1].x, knots_pos[-1].y))

    return len(last_knot_positions)

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()
moves = []
for line in content.splitlines():
    dir, cnt = line.split()
    moves.extend(int(cnt) * [dir])

print(f'Part 1: {move_knots(moves, knots_cnt=1)}')
print(f'Part 2: {move_knots(moves, knots_cnt=9)}')

