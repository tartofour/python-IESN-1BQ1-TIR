#!/usr/bin/python

### FONCTION ###
def affiche_produit(multiplicande, multiplicateur):
    resultat = multiplicande * multiplicateur
    print("{} x {} = {}".format(multiplicande, multiplicateur, resultat))

### MAIN ###
nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un second nombre : "))

affiche_produit(nb1, nb2)
