#!/usr/bin/python

nbreUser = int(input("Entrez un nombre entier en 0 et 15 : "))

bit1 = nbreUser % 2 
bit2 = (nbreUser // 2) % 2 
bit3 = (nbreUser // 4) % 2
bit4 = (nbreUser // 8) % 2

print("{}{}{}{}".format(bit1, bit2, bit3, bit4))
