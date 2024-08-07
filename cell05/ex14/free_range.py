#!/usr/bin/env python3.10

import sys

def main():
	arr = []
	argc = len(sys.argv) - 1
	begin = int(sys.argv[1])
	end = int(sys.argv[2]) + 1

	if argc == 2:
		for begin in range(begin, end):
			arr.append(begin)
		print(arr)
	else:
		print("none")

if __name__ == "__main__":
	main()