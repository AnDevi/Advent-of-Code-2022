#!/usr/bin/python3

from pathlib import Path

class Device:
	def __init__(self):
		self.dirs = []
		self.current_dir = None
	
	def parse_line(self, line):
		line = list(line.split())
		if line[0] == '$':
		
			if line[1] == 'cd':
				if line[2] == '..':
					if self.current_dir.parent_dir is not None:
						self.current_dir = self.current_dir.parent_dir
				else:
					if self.current_dir is None:
						self.current_dir = Dir(line[2])
						pass
					if self.current_dir.name == line[2]:
						pass 
					is_new_dir = True
					for dir in self.current_dir.dirs:
						if dir.name == line[2]:
							self.current_dir = dir
							is_new_dir = False
					if is_new_dir:
						new_dir = Dir(line[2], parent_dir=self.current_dir)
						self.current_dir.addDir(new_dir)
						self.dirs.append(new_dir)
						self.current_dir = new_dir
						
			elif line[1] == 'ls':
				pass
	
		elif line[0] == 'dir':
			pass
		else:
			self.current_dir.addFile(line[1], int(line[0]))

		
class Dir:
	def __init__(self, name, parent_dir = None):
		self.files = []
		self.dirs = []
		self.name = name
		self.parent_dir = parent_dir
		self.level = 0 if parent_dir is None else parent_dir.level + 1

	def addFile(self, name, size):
		self.files.append((name, size))

	def addDir(self, dir):
		self.dirs.append(dir)

	def print(self):
		tab = ''.join([f'\t' for _ in range(self.level)])
		print(f'{tab}- {self.name} (dir)')
		tab += '\t'
		for dir in self.dirs:
			dir.print()
		for file in self.files:
				print(f'{tab}- {file[0]} (file, size={file[1]})')
	def getSize(self):
		size = 0
		for dir in self.dirs:
			dir_size = dir.getSize()
			size += dir_size
		for file in self.files:
			size += file[1]	
		return size


content = Path(Path(__file__).parent.resolve() / 'input.txt').read_text()

device = Device()
MAX_SIZE = 100000
SYSTEM_SIZE = 70000000
NEEDED_SIZE = 30000000

result_part1 = 0
result_part2 = 0

for line in content.splitlines():
	device.parse_line(line)
			
root_dir = device.dirs[0]
root_dir.print()

sizes = [dir.getSize() for dir in device.dirs]

for size in sizes:
	if size <= MAX_SIZE:
		result_part1 += size

root_size = root_dir.getSize()
size_to_released = NEEDED_SIZE - (SYSTEM_SIZE - root_size)

big_enough_sizes = []
for size in sizes:
	if size >= size_to_released:
		big_enough_sizes.append(size)
result_part2 = min(big_enough_sizes)

print(f'Part 1: {result_part1}')

print(f'Part 2: {result_part2}')
