#!/usr/bin/env python3

def main():
	i = 1(int)
	user_input = int(input('Please tell me your age: '))

	print(f'You are currently {user_input} years old.')
	while i <= 3:
		print(f'In {i * 10} years, you\'ll be {user_input + i * 10} years old.')
		i += 1

if __name__ == "__main__":
	main()