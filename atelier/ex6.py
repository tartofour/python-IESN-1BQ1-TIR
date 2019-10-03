#!/usr/bin/python

valeur1 = int(input("Entrez une première valeur : "))
valeur2 = int(input("Entrez une seconde valeur : "))
print("Valeur 1 : {} - Valeur 2 : {}".format(valeur1, valeur2))

valeurTemporaire = valeur2
valeur2 = valeur1
valeur1 = valeurTemporaire
print("Valeur 1 : {} - Valeur 2 : {}".format(valeur1, valeur2))
