#!/usr/bin/python3

from pathlib import Path
import re

content = Path(Path(__file__).parent.resolve() / 'day4.txt').read_text()

LOG_RE = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

full_overlaps = 0
overlaps = 0
for line in content.splitlines():
	m = re.match(LOG_RE, line)
	elfs1 = set([x for x in range(int(m.group(1)), int(m.group(2)) + 1)])
	elfs2 = set([x for x in range(int(m.group(3)), int(m.group(4)) + 1)])

	commons = elfs1 & elfs2

	if len(commons) != 0 and len(commons) == min(len(elfs1), len(elfs2)):
		full_overlaps += 1
	if len(commons) != 0:
		overlaps += 1

print(f'Part 1: {full_overlaps}')
print(f'Part 2: {overlaps}')
