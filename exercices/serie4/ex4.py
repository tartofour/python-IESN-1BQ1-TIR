#!/usr/bin/python

def remove_negatives(lst: list) -> None:
    i = len(lst) - 1
    while i >= 0:
        if lst[i] < 0 :
            del lst[i] 
        i -= 1
    print(lst)

liste = [-23, -2, 28, 23, -23, -12, 1]
remove_negatives(liste)
