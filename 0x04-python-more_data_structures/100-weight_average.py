#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        num = sum(tuple_l[0] * tuple_l[1] for tuple_l in my_list)
        den = sum(tuple_l[1] for tuple_l in my_list)
        return num / den
    return 0
