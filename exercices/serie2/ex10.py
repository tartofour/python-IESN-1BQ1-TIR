#!/usr/bin/env python3

resultat = 0
terme_addition = 0
print("Entrez un nombre négatif pour quitter.")
while terme_addition >= 0:
    terme_addition = int(input("Entrez un terme à additionner "))
    resultat += terme_addition
    print("Résultat de l'addition: {}\n".format(resultat))
