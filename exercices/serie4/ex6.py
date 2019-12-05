#!/usr/bin/python

def swap_min_first(lst: list) -> None:
    i = 0
    min_value = lst[0]
    var_temporaire = 0
    length = len(lst) - 1
    while i < length:
        if lst[i] < min_value: 
            min_value = lst[i]
            min_value_index = i
        i += 1
    var_temporaire = lst[0]
    lst[0] = min_value 
    lst[min_value_index] = var_temporaire
    print(lst)

ma_lst = [9, 8, 7, 6, 1, 5, 4, 3, 2, ]
swap_min_first(ma_lst)
