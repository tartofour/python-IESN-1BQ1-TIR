#!/usr/bin/python
# À mon avis, il y a plus simple.

nbreUser = int(input("Entrez un nombre entier en 0 et 15 : "))

bit1 = nbreUser // (2**3)
bit2 = (nbreUser - bit1 * 2**3) // (2**2)
bit3 = (nbreUser - bit1 * 2**3 - bit2 * 2**2) // (2**1)
bit4 = (nbreUser - bit1 * 2**3 - bit2 * 2**2 - bit3 * 2**1) 

print("{}{}{}{}".format(bit1, bit2, bit3, bit4))
