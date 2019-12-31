#!/usr/bin/env python3

nb_decimal = int(input("Entrez un nombre entier en 0 et 15 : "))
bit1 = nb_decimal // 2**3
bit2 = (nb_decimal - bit1 * 2**3) // 2**2
bit3 = (nb_decimal - bit1 * 2**3 - bit2 * 2**2) // 2**1
bit4 = (nb_decimal - bit1 * 2**3 - bit2 * 2**2 - bit3 * 2**1) 
print("{}{}{}{}".format(bit1, bit2, bit3, bit4))
