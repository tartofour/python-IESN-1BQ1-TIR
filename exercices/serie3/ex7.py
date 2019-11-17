#!/usr/bin/python

def affiche_ip(octet1, octet2, octet3, octet4):
    if is_codable_on_a_byte(octet1) and is_codable_on_a_byte(octet2) and is_codable_on_a_byte(octet3) and is_codable_on_a_byte(octet4):
        print(octet1, octet2, octet3, octet4, sep='.')
    else: 
        print("IP Invalide !")

def is_codable_on_a_byte(nb):
    return True if nb <= 255 else False

nb1 = int(input("Entrez un premier nombre : "))
nb2 = int(input("Entrez un deuxième nombre : "))
nb3 = int(input("Entrez un troisième nombre : "))
nb4 = int(input("Entrez un quatrième nombre : "))

affiche_ip(nb1, nb2, nb3, nb4)
