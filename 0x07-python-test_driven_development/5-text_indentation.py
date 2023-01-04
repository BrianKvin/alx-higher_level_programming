#!/usr/bin/python3
#  Module composed by a function that prints 2 new lines after ".?:" characters


def text_indentation(text):
    """
    Function that prints 2 new lines after ".?:" characters
    Args: text - input string
    Returns:no return
    Raises: TypeError - if text is not a string
    """
    if isinstance(text) is not str:
        raise TypeError("text must be a string")
    list = ['.', '?', ':']
    for word in text:
        if word in list:
            print(word, end="")
            print()
            print()
        else:
            print(word, end="")
