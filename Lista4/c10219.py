from sys import stdin
from math import comb

for linha in stdin:
    a, b = list(map(int, linha.split()))
    result = comb(a, b)
    print(len(str(result)))
