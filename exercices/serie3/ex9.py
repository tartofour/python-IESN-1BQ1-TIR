#!/usr/bin/python

def inverseur_casse(lettre):
    valeur_unicode = ord(lettre)
    if valeur_unicode > 90:
        return chr(valeur_unicode - 32)
    else:
        return chr(valeur_unicode + 32)

lettre = input("Entrez une lettre majuscule ou minuscule : ")
print(inverseur_casse(lettre))
