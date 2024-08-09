#!/usr/bin/env python3

import sys

def main():
	argc = len(sys.argv) - 1
	if argc > 1:
		print(f"parameters: {argc}")
		for i in range(1, argc + 1):
			print(f"{sys.argv[i]}: {len(sys.argv[i])}")
	else:
		print("none")

main()