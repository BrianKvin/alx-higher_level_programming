#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print()
"""
def uppercase(str):
    for i in str:
        if ord(i) >= 65 and ord(i) <= 90:
            print(f"{i}", end="")
        else:
            i = chr(ord(i) - 32)
            print(f"{}", end="")
 uppercase():wq
"""
