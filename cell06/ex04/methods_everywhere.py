#!/usr/bin/env python3

import sys

def shrink(param):
	x = slice(0,8)
	print(param[x])

def enlarge(param:str):
	x = 8 - len(param)
	for i in range(0, x):
		param += "Z"
	print(param)

def main():
	argc = len(sys.argv)

	if argc != 1:
		for i in range(1, argc):
			if len(sys.argv[i]) > 8:
				shrink(sys.argv[i])
			else:
				enlarge(sys.argv[i])
	else:
		print("none")

main()