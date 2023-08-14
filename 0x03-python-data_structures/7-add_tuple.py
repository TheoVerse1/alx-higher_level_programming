#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by extending them with zeros
    tuple_a += (0, 0)
    tuple_b += (0, 0)
    
    # Calculate the sum of the first elements and the sum of the second elements
    sum_first = tuple_a[0] + tuple_b[0]
    sum_second = tuple_a[1] + tuple_b[1]
    
    # Create a new tuple with the calculated sums
    tuple_c = (sum_first, sum_second)
    return tuple_c
