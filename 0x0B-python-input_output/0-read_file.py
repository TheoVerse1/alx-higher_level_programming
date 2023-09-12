#!/usr/bin/python3

def read_file(filename=""):
    """
    Reads the content of a text file and prints it to stdout.

    Args:
        filename (str): The name of the text file to be read.
                        Default is an empty string.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
