#!/usr/bin/env python3

taux_change_dollars = float(input("Taux de change : "))
montant_euros = float(input("Montant en Euros : "))
montant_dollars = montant_euros * taux_change_dollars
print( "{} Euros vaut {:.2f} Dollars".format(montant_euros, montant_dollars))
