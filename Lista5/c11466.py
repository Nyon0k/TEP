from math import sqrt

def addInDic(maiorPrimo):
    dic[maiorPrimo] = dic.get(maiorPrimo, 0)+1

n = abs(int(input()))
while n != 0:
    dic = {}
    maiorPrimo = -1
    while n%2 == 0:
        maiorPrimo = 2
        addInDic(maiorPrimo)
        n /= 2
    while n%3 == 0:
        maiorPrimo = 3
        addInDic(maiorPrimo)
        n /= 3
    for i in range(5, int(sqrt(n))+1, 6):
        while n%i == 0:
            maiorPrimo = i
            addInDic(maiorPrimo)
            n /= i
        while n%(i+2) == 0:
            maiorPrimo = i+2
            addInDic(maiorPrimo)
            n /= maiorPrimo
    if n > 4:
        maiorPrimo = int(n)
        addInDic(maiorPrimo)
    if len(dic) < 2:
        maiorPrimo = -1
    print(maiorPrimo)
    n = abs(int(input()))
