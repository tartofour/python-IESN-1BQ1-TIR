#!/usr/bin/python

def split_even_odd(lst: list) -> tuple:
    i = 0
    lst_even_index = []
    lst_odd_index = []
    length = len(lst)
    while i < length:  
        if i % 2 == 0:
            lst_even_index.append(lst[i])
        else:
            lst_odd_index.append(lst[i])
        i += 1
    return (lst_even_index,lst_odd_index)

liste = [22, 21, 35, 53, 22, 24]
print(liste)
print(split_even_odd(liste))
