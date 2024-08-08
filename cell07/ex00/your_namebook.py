#!/usr/bin/env python3

def array_of_names(dict):
	array = []
	for i in dict:
		array.append(f"{i.capitalize()} {dict[i].capitalize()}")

	return (array)

persons = {
	"jean": "valjean",
	"grace": "hopper",
	"xavier": "niel",
	"fifi": "brindacier"
}

print(array_of_names(persons))