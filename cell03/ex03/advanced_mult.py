#!/usr/bin/env python3
import sys

def main():
	i = 0
	x = 0

	if len(sys.argv) != 1:
		exit(print("none"))

	while i <= 10:
		print(f'Table de', str(i) + ':', end='')
		while x <= 10:
			if x != 10:
				print('', i * x,  end='')
			else:
				print('', i * x)
			x += 1
		i += 1
		x = 0

if __name__ == "__main__":
	main()