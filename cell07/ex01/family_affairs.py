#!/usr/bin/env python3

def find_the_redheads(dict):
    print(dict.keys())
    list_key = dict.tolist()
    print(list_key)

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))