#!/usr/bin/python
# Code dégueu ?

def selection_sort(lst: list) -> None:
    length = len(lst)
    start_index = 0
    min_value_index = 0
    i = 0
    while start_index < length:
        min_value = lst[start_index]
        while i < length:
            if lst[i] < min_value: 
                min_value = lst[i]
                min_value_index = i
            i += 1
        var_temporaire = lst[start_index]
        lst[start_index] = min_value 
        lst[min_value_index] = var_temporaire
        start_index += 1
        i = start_index
    print(lst)

ma_lst = [9, 8, 7, 6, 1, 5, 4, 3, 2]
selection_sort(ma_lst)
