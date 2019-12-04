#!/usr/bin/python

def replace_non_zero(lst: list) -> None:
    length = len(lst)
    i = 0
    while i < length:
        if lst[i] != 0:
           lst[i] = 1 
        i += 1
    print(lst)

liste = [2, 0, 3, 0, 0, 4, 5, 4]
replace_non_zero(liste)
