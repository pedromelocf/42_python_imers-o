#!/usr/bin/env python3
def filter_redheads(person):
    if person[1] == "red":
        return True
    else:
        return False

def find_the_redheads(obj):
    result = dict(filter(filter_redheads, obj.items()))
    print(list(result.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

find_the_redheads(dupont_family)