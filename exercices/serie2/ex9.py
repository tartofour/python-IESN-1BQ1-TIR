#!/usr/bin/env python3

multiplicande = int(input("Entrez un nombre entier afin d'afficher sa table de multiplication : "))
i = 1 
while i <= 10:
    print("{} x {} = {}".format(multiplicande, i, multiplicande * i))
    i += 1
