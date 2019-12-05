#!/usr/bin/python

def merge_uniques(lst_from: list, lst_to: list) -> None:
    added_tuple = 0
    length_lst_from = len(lst_from)
    length_lst_to = len(lst_to)
    i = 0
    while i < length_lst_from:
        if lst_from[i] not in lst_to:
            lst_to.append(lst_from[i])
            added_tuple += 1
        i+=1    
    print(added_tuple)

liste1 = [(1, 2, 3), ( 4, 5, 6), (7, 8, 9), (10, 11, 12), (19, 20, 21)]
liste2 = [(7, 8, 9), (10, 11, 12), (13, 14, 15), (16, 17, 18)]
merge_uniques(liste1, liste2)
