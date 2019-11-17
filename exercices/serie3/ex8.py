#!/usr/bin/python

def nb_jours_mois(mois, est_bissextile=False):
    if mois == "avril" or mois == "juin" or mois == "septembre" or mois == "novembre":
        return 30
    elif mois == "fevrier":
        return 29 if est_bissextile == True else 28
    else:
        return 31
    
mois = input("Entrez un mois pour connaître le nombre de jours qui le constitue (sans accent) : ")
bissextile = input("L'année est-elle bissextile ? (o/n) : ")

if bissextile == "o":
    print(nb_jours_mois(mois, True))
else:
    print(nb_jours_mois(mois))
