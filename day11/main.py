#!/usr/bin/python3

from pathlib import Path
import re
import copy

class Monkey:
    def __init__(self, id: int, items: list(), sign: str, number: str, test: int, if_true: int, if_false: int):
        self.id = id
        self.items = items
        self.sign = sign
        self.number = number
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.held = 0

    def __str__(self):
        return f'Monkey {self.id}:\nItems: {self.items}\nOperation: new = old {self.sign} {self.number}\nTest - divided by {self.test}:\n\tIf true: {self.if_true}\n\tIf False: {self.if_false}\n'
    def __repr__(self):
        return f'Monkey {self.id}:\nItems: {self.items}\nOperation: new = old {self.sign} {self.number}\nTest - divided by {self.test}:\n\tIf true: {self.if_true}\n\tIf False: {self.if_false}\n'

content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text().split('\n\n')

def play(monkeys, rounds, do_worry):

    monkey_mod = 1
    for m in monkeys:
        monkey_mod *= m.test

    for x in range(rounds):
        for m in monkeys:
            while len(m.items) != 0:
                m.held += 1
                item = m.items.pop(0)
                number = item if m.number == 'old' else int(m.number)
                item = item * number if m.sign == '*' else item + number
                if not do_worry:
                    item = item // 3
                else:
                    item = item % monkey_mod
                thrown_to = m.if_true if item % m.test == 0 else m.if_false
                monkeys[thrown_to].items.append(item)

    inspections = [m.held for m in monkeys]
    inspections = sorted(inspections)

    return inspections[-1] * inspections[-2]


monkeys = list()
for m in content:
    lines = m.splitlines()
    id = int(re.findall(r'(\d+)', lines[0])[0])
    items = [int(a) for a in re.findall("(\d+)", lines[1])]
    sign, number = re.findall(r'(\+|\*)\s(old|\d+)', lines[2])[0]
    test = int(re.findall(r'(\d+)', lines[3])[0])
    if_true = int(re.findall(r'(\d+)', lines[4])[0])
    if_false = int(re.findall(r'(\d+)', lines[5])[0])
    monkeys.append(Monkey(id, items, sign, number, test, if_true, if_false))

monkeys_p1 = copy.deepcopy(monkeys)
monkeys_p2 = copy.deepcopy(monkeys)

print(f'Part 1: {play(monkeys_p1, 20, False)}')
print(f'Part 2: {play(monkeys_p2, 10000, True)}')
