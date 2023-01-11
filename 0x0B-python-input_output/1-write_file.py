#!/usr/bin/python3
"""This module defines a file-writing function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file
    Args: filr name - file to be written
    text (str): string to be written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
