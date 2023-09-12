#!/usr/bin/python3
"""A function that reads from a file"""


def read_file(filename=""):
    """Reads the content of a text file and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
