#!/usr/bin/env python3

import sys

def main():
	argc = len(sys.argv)
	if argc == 2:
		print(sys.argv[1].upper())
	else:
		print("none")

main()