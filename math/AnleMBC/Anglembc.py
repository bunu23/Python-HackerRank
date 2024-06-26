# Enter your code here. Read input from STDIN. Print output to STDOUT

from math import sqrt
from math import acos
from math import degrees

AB = int(input())
BC = int(input())

AC = sqrt(AB ** 2 + BC ** 2)

BM = AC / 2

angle = acos(BC / (2*BM))

print("{}{}".format(round(degrees(angle)), chr(176)))
