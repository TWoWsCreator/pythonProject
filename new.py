from functools import reduce
from math import gcd


numbers = []
for _ in range(int(input())):
    numbers.append(int(input()))
    print(numbers)
    print('1')
    print('4')
print(reduce(gcd, numbers))