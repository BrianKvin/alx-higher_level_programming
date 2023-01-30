#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')

"""
for i in range(ord("a"), ord("z") + 1):
    if i is not (ord("e")) and i is not (ord("q")):
        print("{}".format(chr(i), end="")
"""
