#!/usr/bin/python

def common_pairs(d1: dict, d2: dict) -> list:
    lst_common_value = []
    for elmt in d1:
        if elmt in d2 and d1[elmt] == d2[elmt]: 
                tpl_common_value = elmt, d1[elmt]
                lst_common_value.append(tpl_common_value)
    return lst_common_value


d1 = {1 : "Hi", 2 : "Bonjour", 3 : "Prout", 4 : "Coucou"}
d2 = {1 : "Hi", 2 : "Aurevoir", 3 : "Prit", 4 : "Coucou"}
print(common_pairs(d1, d2))
