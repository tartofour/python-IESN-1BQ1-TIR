#!/usr/bin/python

### FONCTION ###
def est_premier(nb: int) -> bool:
    i = 2
    while i < ((nb**1/2)+1):
        if nb % i == 0:
            return False 
        i+=1

    return True
        
### MAIN ###
nb = int(input("Entrez un nombre entier positif : "))
print(est_premier(nb))
