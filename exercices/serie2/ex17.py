#!/usr/bin/python

### FONCTION ###
def affiche_echiquier():
    for i in range(8):
        if i %2 == 0:
            print("_ # _ # _ # _ #")
        else: 
            print("# _ # _ # _ # _")

### MAIN ###
affiche_echiquier()
