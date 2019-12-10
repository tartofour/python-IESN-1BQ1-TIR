#!/usr/bin/python

### PAS FINI !!! ###

def common_pairs(d1: dict, d2: dict) -> list:
    lst_common_value = []
    for elmt in d1:
        if elmt in d2:
        lst_common_value.append((elmt))
    return lst_common_value


d1 = {1 : "Hi", 2 : "Bonjour", 3 : "Prout"}
d2 = {1 : "Hi", 2 : "Aurevoir", 3 : "Prit"}
print(common_pairs(d1, d2))
