#!/usr/bin/env python3

nb_decimal = int(input("Entrez un nombre entier en 0 et 15 : "))
bit1 = nb_decimal % 2 
bit2 = (nb_decimal // 2) % 2 
bit3 = (nb_decimal // 4) % 2
bit4 = (nb_decimal // 8) % 2
print("{}{}{}{}".format(bit1, bit2, bit3, bit4))
