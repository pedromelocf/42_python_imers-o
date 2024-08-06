#!/usr/bin/env python3

def main():
	first_number = int(input("Enter the first number:"))
	second_number = int(input("Enter the second number:"))
	result = int(first_number * second_number)

	print(first_number, "x", second_number, "=", result)
	if result > 0:
		print("This number is positive.")
	elif result < 0:
		print("This number is negative.")
	else:
		print("This number is positive and negative.")

if __name__ == "__main__":
	main()