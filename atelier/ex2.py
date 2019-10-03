#!/usr/bin/python

tauxChangeDollard = float(input("Taux de change : "))
montantEuros = float(input("Montant en Euros : "))
montantDollards = montantEuros * tauxChangeDollard
print( "{} Euros vaut {} Dollards".format(montantEuros, montantDollards))

        
