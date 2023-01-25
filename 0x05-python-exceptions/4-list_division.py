#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element
    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions."""
    new_list = []
    for i in range(list_length):
        try:
            x = my_list_1[i] / my_list_2[i]
        except TypeError:
            x = 0
            print("Wrong type")
        except ZeroDivisionError:
            x = 0
            print("division by 0")
        except IndexError:
            x = 0
            print("out of range")
        finally:
            new_list.append(x)
        return (new_list)
