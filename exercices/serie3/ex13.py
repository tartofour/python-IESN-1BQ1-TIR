#!/usr/bin/python

def sqrt(nb: int) -> float:
    """ Retourne la racine carré de nb
    
    Args:
        nb (int): nombre sur lequel s'applique la racine carré 

    Return:
        racine carré de nb (float)    
    
    """
    return nb**(1/2)

nb = int(input("Entrez un nombre : "))
print(sqrt(nb))


