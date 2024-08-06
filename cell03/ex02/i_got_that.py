#!/usr/bin/env python3

def main():
	stop = "STOP"
	user_input = input("What you gotta say? : ")
	
	while True:
		user_input = input("I got that! Anything else? : ")
		if user_input == stop:
			break

if __name__ == "__main__":
	main()