#!/usr/bin/env python3

def main():
	i = 0
	user_input = int(input("Enter a number\n"))
	while i <= 9:
		print(i, "x", user_input, "=", user_input * i)
		i += 1

if __name__ == "__main__":
	main()