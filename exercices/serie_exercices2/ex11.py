#!/usr/bin/python

nb_user = int(input("Entrez un nombre afin de calculer sa factorielle : "))
resultat = 1

while nb_user > 0:
    resultat *= nb_user 
    nb_user -= 1

print(resultat)
