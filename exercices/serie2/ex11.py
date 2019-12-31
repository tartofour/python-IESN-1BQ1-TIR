#!/usr/bin/env python3

nb = int(input("Entrez un nombre afin de calculer sa factorielle : "))
resultat = 1
while nb > 0:
    resultat *= nb 
    nb -= 1
print(resultat)
