#!/usr/bin/env python3

valeur1 = int(input("Entrez une première valeur : "))
valeur2 = int(input("Entrez une seconde valeur : "))
print("Valeur 1 : {} - Valeur 2 : {}".format(valeur1, valeur2))

# Invertion des valeurs
valeur_temporaire = valeur2
valeur2 = valeur1
valeur1 = valeur_temporaire
print("Valeur 1 : {} - Valeur 2 : {}".format(valeur1, valeur2))
