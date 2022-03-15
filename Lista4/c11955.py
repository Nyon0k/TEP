from math import comb
n = int(input())

for i in range(n):
    term1 = []
    term2 = []
    grauParcial = []
    expression = input()
    tam = len(expression)
    index = 0
    flag1 = 0
    flag2 = 0
    for c in expression:
        if c != '(' and flag1 == 0:
            if c != '+':
                term1.append(c)
            else:
                flag1 = 1
        if c != '+' and flag2 == 0 and flag1 == 1:
            if c != ')':
                term2.append(c)
            else:
                flag2 = 1
        if c != ')' and flag1 == 1 and flag2 == 1:
            if c == ' ':
                break
            if c != '^':
                grauParcial.append(c)
    termo1 = ''.join(term1)
    termo2 = ''.join(term2)
    grau = ''.join(grauParcial)
    grau = int(grau)
    if grau == 1:
        result = str(termo1)
    else:
        result = str(termo1)+'^'+str(grau)
    for j in range(1,grau):
        result += '+'+str(comb(grau,j))
        if grau-j == 1:
            result += '*'+str(termo1)
        else:
            result += '*'+str(termo1)+'^'+str(grau-j)
        if j == 1:
            result += '*'+str(termo2)
        else:
            result += '*'+str(termo2)+'^'+str(j)
    if grau == 1:
    	result += '+'+str(termo2)
    else:
    	result += '+'+str(termo2)+'^'+str(grau)
    print('Case '+str(i+1)+': '+result)
