#!/usr/bin/python

def print_tails(lst: list) -> None:
    length = len(lst)
    start_index = 0
    i = 0
    while start_index < length:
        while i < length:
            print(lst[i])
            i += 1
        start_index += 1
        i = start_index
        
lst = [1, 2, 3, 4]
print_tails(lst)

