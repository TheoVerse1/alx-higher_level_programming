#!/usr/bin/python3
"""
Args:
    filename (str): The name of the text file to be read.
                    Default is an empty string.
"""
def read_file(filename=""):
    """Reads the content of a text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
