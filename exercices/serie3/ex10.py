#!/usr/bin/python

### FONCTIONS ###
def est_bissextile(annee):
    if annee % 4 == 0 and (annee % 100 != 1 or annee % 400 == 0):
        return True
    else:
        return False

def nb_jours_mois(mois, annee):
    if mois == "janvier" or mois == "mars" or mois == "mai" or mois == "juillet" or mois == "aout" or mois == "octobre" or mois == "decembre":
        return 31
    elif mois =="fevrier":
        return 29 if est_bissextile(annee) else 28
    else:
        return 30

### MAIN ###
mois = input("Entrez un mois pour connaître le nombre de jours qui le compose : ")
annee = int(input("Entrez un année : "))

print(nb_jours_mois(mois, annee))
