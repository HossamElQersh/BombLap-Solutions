# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import math



def func4(x, y, n):
    z = ((x - y) / 2) + y
    prev_z = None
    while True:
        if z < n:
            y = z + 1
        elif z > n:
            x = z - 1
        else:
            return prev_z

        prev_z = z
        z = ((x - y) / 2) + y

# Example usage:







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
