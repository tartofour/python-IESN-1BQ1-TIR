#!/usr/bin/python

nbreDec = int(input("Entrez un nombre en 0 et 15 : "))
resultatBin = ''

if nbreDec == 0 :
    resultatBin += '0'

while nbreDec != 0:
    if nbreDec % 2 == 1:
        resultatBin += '1'
        nbreDec = nbreDec // 2
    else:
        resultatBin += '0'
        nbreDec = nbreDec // 2

print(resultatBin[::-1])


