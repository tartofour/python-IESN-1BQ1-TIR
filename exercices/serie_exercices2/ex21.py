#!/usr/bin/python

### FONCTIONS ###
def tic():
    print("Tic")

def tac():
    print("Tac")

### MAIN ###
global nb_secondes
nb_secondes = int(input("Entrez un nombre de seconde(s) : "))

while nb_secondes > 0:
    if nb_secondes % 2 == 0:
        tic()
    else: 
        tac()

    nb_secondes -= 1

