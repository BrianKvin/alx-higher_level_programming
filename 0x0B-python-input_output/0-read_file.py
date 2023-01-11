#!/usr/bin/python3
"""This module defines a text file-reading function"""


def read_file(filename=""):
    """
        Prints the contents of a UTF8 text file
        filename (any) to be read
    """
    with open(filename, mode='r', encoding="utf-8") as f:
        print(f.read(), end="")


"""
#!/usr/bin/python3


def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as f1:
        print(f.read(), end="")
"""
