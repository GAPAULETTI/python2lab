import sys

for p in sys.path:
    print(p)


from sys import path

path.append('d:\\PythonEssential2\\PythonM1\\modules')

from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))

import math
print("Actually")
result = math.e != math.pow(2,4)
print(int(result))

from random import randint

for i in range(2):
    print(randint(1,2), end='')

from sys import platform

platform.version()