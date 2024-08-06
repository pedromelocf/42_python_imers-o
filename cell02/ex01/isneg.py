#!/usr/bin/env python3

def main():
	user_number = int(input())
	if user_number > 0:
		print("This number is positive.")
	elif user_number < 0:
		print("This number is negative.")
	else:
		print("This number is both positive and negative.")

if __name__ == "__main__":
	main()