#!/usr/bin/python

def is_empty(lst: list) -> bool:
    return True if not lst else False

def print_max(lst: list) -> None:
    if is_empty(lst):
        print("ERREUR : La liste est vide.")
    else:
        print(max(lst))

liste = []
#liste = [4, 76, 3, 65, 235, 236, 124, 121, 3, 5]
print_max(liste)
