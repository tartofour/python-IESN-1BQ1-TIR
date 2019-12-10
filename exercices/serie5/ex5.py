#!/usr/bin/python

def sort_keys(d: dict) -> tuple:
    int_dict = {}
    str_dict = {}
    for elmt in d:
        if type(elmt) is str:
            str_dict[elmt] = d[elmt] 
        elif type(elmt) is int:
            int_dict[elmt] = d[elmt]
    return int_dict, str_dict

d = {1 : "Hello", "deux" : "its me", 3 : "Mdr", "quatre" : "ptdr"}
print(sort_keys(d))

