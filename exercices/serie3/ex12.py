#!/usr/bin/python

### FONCTION ###
def division(nb1: int, nb2: int) -> float:
    return nb1 / nb2

### MAIN ###
diviseur = int(input("Entrez le dividende : "))
dividende = int(input("Entrez le diviseur : "))

print(division(diviseur, dividende))
