#!/usr/bin/env python3

def main():
	original_array = [2, 8, 9, 48, 8, 22, -12, 2]
	new_array = []
	i = 0

	while i < len(original_array):
		if original_array[i] > 5:
			new_array.append(original_array[i] + 2)
		i += 1

	display = set(new_array)
	print(original_array)
	print(display)

if __name__ == "__main__":
	main()