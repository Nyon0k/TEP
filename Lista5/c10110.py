from math import sqrt

n = int(input())
while n != 0:
    raiz = sqrt(n)
    if raiz == int(raiz):
        print('yes')
    else:
        print('no')
    n = int(input())
