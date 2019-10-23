#!/usr/bin/python

### FONCTIONS ###
def ligne_impair():
    print("# _ # _ # _ # _")

def ligne_pair():
    print("_ # _ # _ # _ #")

def affiche_echiquier():
    for i in range(8):
        if i %2 == 0:
            ligne_pair()
        else: 
            ligne_impair()

### MAIN ###
affiche_echiquier()
