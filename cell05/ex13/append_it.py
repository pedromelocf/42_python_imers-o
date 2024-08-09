#!/usr/bin/env python3.10

import sys

def main():
	argc = len(sys.argv)
	argv = sys.argv
	argv.pop(0)

	if argc == 1:
		exit(print("none"))

	for word in argv:
		match word.endswith("ism"):
			case False:
				print(word + "ism")
			case _:
				continue


main()