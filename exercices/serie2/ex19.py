#!/usr/bin/python

### FONCTION ###
def is_square():
    global nb
    racine = nb**(1/2)

    if racine**2 == nb: 
        print("Il s'agit bien d'une racine.")

### MAIN ###
nb = int(input("Entrez un nombre entier : ")) 
is_square()
