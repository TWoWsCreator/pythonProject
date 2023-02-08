from functools import reduce
from math import gcd


numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
print(reduce(gcd, numbers))