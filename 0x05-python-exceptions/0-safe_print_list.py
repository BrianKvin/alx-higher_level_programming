#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):

    """Print x elements of a list.
    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.
    Returns:
        The number of elements printed.
    """
    printed_elements = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed_elements += 1
            print()
    except IndexError:
        print()
        return printed_elements
