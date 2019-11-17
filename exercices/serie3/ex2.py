#!/usr/bin/python

def greater_number(nb1, nb2):
    return nb1 if nb1 > nb2 else nb2

nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un second nombre : "))

print(greater_number(nb1, nb2))
