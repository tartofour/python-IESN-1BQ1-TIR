#!/usr/bin/python
# PAS FINI



def merge_uniques(lst_from: list, lst_to: list) -> None:
    added_tuple = 0
    length_lst_from = len(lst_from)
    length_lst_to : len(lst_to)

    for i in lst_to:
        while j < length_lst_to:
            if lst_from[i] not in lst_to[j]:
                lst_to.append(lst_from[i])
                added_tuple += 1
            j+=1
        i+=1
    
    print(added_tuple)
    
liste1 = [(1, 2, 3)(4, 5, 6)(7, 8, 9)(10, 11, 12)]
liste2 = [(7, 8, 9)(10, 11, 12)(13, 14, 15)(16, 17, 18)]

