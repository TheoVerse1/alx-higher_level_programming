#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    if idx < 0 or idx >= len(copy):
        return copy
    else:
        for i in range(0, len(copy)):
            if i == idx:
                copy[idx] = element
                return copy
