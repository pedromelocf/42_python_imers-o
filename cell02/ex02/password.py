#!/usr/bin/env python3

def main():
	password = "Python is awesome"
	user_input = input()
	if user_input == password:
		print("ACCESS GRANTED")
	else:
		print("ACCESS DENIED")

if __name__ == "__main__":
	main()