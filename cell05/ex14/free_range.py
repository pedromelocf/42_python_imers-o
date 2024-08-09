#!/usr/bin/env python3.10

import sys

def main():
	argc = len(sys.argv) - 1

	if argc == 2:

		begin = int(sys.argv[1])
		end = int(sys.argv[2]) + 1

		arr = [begin for begin in range(begin, end)]
		
		print(arr)
	else:
		print("none")

main()