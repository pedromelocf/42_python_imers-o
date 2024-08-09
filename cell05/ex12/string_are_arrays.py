#!/usr/bin/env python3

import sys

def main():
	argc = len(sys.argv) - 1
	count = 0

	if argc == 1:
		for i in range(0, len(sys.argv[1])):
			if sys.argv[1][i] == "z":
				print("z", end='')
				count += 1
		if count == 0:
			print("none", end='')
	else:
		print("none", end='')
	print("")

main()