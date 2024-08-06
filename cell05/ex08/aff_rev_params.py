#!/usr/bin/env python3

import sys

def main():
	argc = len(sys.argv)
	i = len(sys.argv) - 1

	if argc > 2:
		while i > 0:
			print(sys.argv[i])
			i -= 1
	else:
		print("none")

if __name__ == "__main__":
	main()