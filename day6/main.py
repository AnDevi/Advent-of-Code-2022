#!/usr/bin/python3

from pathlib import Path

content = list(Path(Path(__file__).parent.resolve() / 'input.txt').read_text())

def find_packet_start(packet, packet_len):
	sub_packet = packet[:packet_len]
	for i in range(packet_len, len(content) -1 , 1):
		sub_packet = sub_packet[1:]
		sub_packet.append(content[i])
		if len(sub_packet) == len(set(sub_packet)):
			return i + 1

start = find_packet_start(content, 4)
print(f'Part 1: {start}')

start = find_packet_start(content, 14)
print(f'Part 2: {start}')
