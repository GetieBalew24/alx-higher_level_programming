#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_result = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            list_result[count] = True
        else:
            list_result[count] = False
    return(list_result)
