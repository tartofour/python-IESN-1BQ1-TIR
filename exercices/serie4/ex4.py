#!/usr/bin/python

def remove_negatives(lst: list) -> None:
    lst2 = []
    for elt in lst:
        if elt >= 0 :
            lst2.append(elt)
    print(lst2)

liste = [-23, -2, 28, 23, -23, -12, 1]
remove_negatives(liste)
