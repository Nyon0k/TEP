from sys import stdin
for linha in stdin:
    a, b = list(map(int, linha.split()))
    if 4*a < b:
        res = 10*a-2*b
    elif 3*a < 2*b:
        res = 8*a-4*b
    elif 2*a < 3*b:
        res = 6*a-6*b
    elif a < 4*b:
        res = 3*a-9*b
    else:
        print('Deficit')
        continue
    if res > 0:
        print(res)
    else:
        print('Deficit')
