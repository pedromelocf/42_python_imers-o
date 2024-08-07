#!/usr/bin/env python3

import sys

def main():
	argc = len(sys.argv)

	if argc != 1:
		for i in range(1, argc):
			print(downcase_it(sys.argv[i]))
	else:
		print("none")

def downcase_it(message):
	return str(message).lower()

main()