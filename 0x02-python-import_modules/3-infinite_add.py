#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys


"""
    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[i + 1])
    print("{}".format(total))
"""
    x = len(sys.argv) - 1
    add = 0

    for i in range(x):
        add += (int(sys.argv[i + 1]))
    print("{:d}".format(add))
