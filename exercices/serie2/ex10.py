#!/usr/bin/python

resultat = 0
continuer = True 

while continuer:
    nb_a_addictionner = int(input("Entrez un nombre : "))
    
    if nb_a_addictionner < 0:
        continuer = False
        print("Fermeture du programme.")
    else:
        resultat += nb_a_addictionner
        print("Résultat : {}".format(resultat))
