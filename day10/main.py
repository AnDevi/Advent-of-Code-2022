#!/usr/bin/python3

from pathlib import Path
from enum import Enum

content = Path(Path(__file__).parent.resolve() / 'day10.txt').read_text().splitlines()

class Action(Enum):
    IDLE = 1
    ADDING = 2

strength = 0
cycles = 1
register = 1
value_to_add = 0
instruction = ''
curr_action = Action.IDLE
CRT = []

while cycles != 241 and len(content) != 0:
    if (cycles - 20) % 40  == 0:
        strength += cycles * register

    position = len(CRT) % 40
    if position >= register - 1 and position <= register + 1:
        CRT.append('#')
    else:
        CRT.append('.')

    if curr_action is Action.ADDING:
        register += value_to_add
        curr_action = Action.IDLE
    else:
        instruction = str(content[0])
        if 'noop' in instruction:
            content.pop(0)
        elif 'addx' in instruction and curr_action is Action.IDLE:
            content.pop(0)
            value_to_add = int(instruction.split()[1])
            curr_action = Action.ADDING
    cycles += 1

print(f'Part 1: {strength}')

print(f'Part 2:')
line = ''
for i in range(len(CRT)):
    if (i + 1) % 40 == 0:
        print(line)
        line = ''
    else:
        line += CRT[i]

