#!/usr/bin/env python3

import sys

def main():
	arr = ['Alexandra', 'Wil', None , 42]

	for i in range(0 , 4):
		greetings(arr[i])

def greetings(argument: any = None):
	if argument is None:
		print(f"Hello, noble stranger.")
	elif isinstance(argument, str):
		print(f"Hello, {argument}.")
	else:
		print("Error! It was not a name.")

main()
