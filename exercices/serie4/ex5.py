#!/usr/bin/python

def split_even_odd(lst: list) -> tuple:
    i = 0
    lst_even = []
    lst_odd = []
    length = len(lst)
    while i < length:  
        if i % 2 == 0:
            lst_even.append(lst[i])
        else:
            lst_odd.append(lst[i])
        i += 1
    return (lst_even,lst_odd)

liste = [22, 21, 35, 53, 22, 24]
print(liste)
print(split_even_odd(liste))




