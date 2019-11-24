#!/usr/bin/python

def division(nb1: int, nb2: int) -> float:
    """Retourne le resultat de la division de nb1 par nb2.
    
    Args: 
        nb1 (int): Le dividende
        nb2 (int): Le diviseur

    Return:
        Résultat de la division (float) 

    """
    return nb1 / nb2

diviseur = int(input("Entrez le dividende : "))
dividende = int(input("Entrez le diviseur : "))
print(division(diviseur, dividende))
