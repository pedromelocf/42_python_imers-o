#!/usr/bin/env python3

import sys
import re

def main():
	i = len(sys.argv)
	if i == 3:
		list = re.findall(sys.argv[1], sys.argv[2])
		print(len(list))
	else:
		print("none")

main()