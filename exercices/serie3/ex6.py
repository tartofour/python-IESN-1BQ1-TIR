#!/usr/bin/python

def affiche_table(multiplicande, debut=1, fin=10):
    while debut <= fin:
        resultat = multiplicande * debut
        print("{} x {} = {}".format(multiplicande, debut, resultat))
        debut += 1

nb = int(input("La table de multiplication de quel nombre souhaitez-vous afficher? : "))
debut = int(input("Entrez le multiplicateur minimum : "))
fin = int(input("Entrez le multiplicateur maximum : "))

affiche_table(nb, debut, fin)

