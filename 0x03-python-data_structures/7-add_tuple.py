#!/usr/bin/python3

# Define a function that takes two optional tuple arguments
def add_tuple(tuple_a=(), tuple_b=()):
    # Check if both tuples are non-empty
    if tuple_a and tuple_b:
        # Check different cases based on tuple lengths
        
        # Case 1: Both tuples have less than 2 elements
        if len(tuple_a) < 2 and len(tuple_b) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = 0
        
        # Case 2: tuple_a has less than 2 elements, tuple_b has 2 or more
        elif len(tuple_a) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = 0 + tuple_b[1]
        
        # Case 3: tuple_b has less than 2 elements, tuple_a has 2 or more
        elif len(tuple_b) < 2:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + 0
        
        # Case 4: Both tuples have 2 or more elements
        else:
            a = tuple_a[0] + tuple_b[0]
            b = tuple_a[1] + tuple_b[1]
        
        # Create a new tuple with the calculated values
        tuple_c = (a, b)
        return tuple_c
    else:
        # Handle cases where one or both tuples are empty
        
        # Case 5: Both tuples are empty
        if not tuple_b and not tuple_a:
            tuple_c = (0, 0)
            return tuple_c
        
        # Case 6: Only tuple_a is empty
        elif not tuple_a:
            return tuple_b
        
        # Case 7: Only tuple_b is empty
        else:
            return tuple_a
