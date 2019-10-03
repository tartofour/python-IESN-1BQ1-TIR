#!/usr/bin/python

tauxChangeDollars = 1.09
montantEuros = float(input("Montant en Euros : "))
montantDollars = montantEuros * tauxChangeDollars
print( "{} Euros vaut {:.2f} Dollars".format(montantEuros, montantDollars))

        
