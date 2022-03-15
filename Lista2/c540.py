from sys import stdin
from collections import deque as d
contador = 1
flag = True
while flag:
    timeTotal = {}
    timeFila = {}
    dq = d()
    filas = int(stdin.readline())
    if filas == 0:
        flag == False
        break
    for fila in range(filas):
        timeFila[fila] = d()
        t = stdin.readline().split()
        for cont in range(1, int(t[0])+1):
            timeTotal[t[cont]] = fila
    print('Scenario #'+str(contador))
    contador = contador+1
    for linha in stdin:
        linha = linha.split()
        if linha[0] == "ENQUEUE":
            tam = len(timeFila[timeTotal[linha[1]]])
            if tam == 0:
                dq.append(timeTotal[linha[1]])
            timeFila[timeTotal[linha[1]]].append(linha[1])
        elif linha[0] == "DEQUEUE":
            print(timeFila[dq[0]].popleft())
            tam = len(timeFila[dq[0]])
            if tam == 0:
                dq.popleft()
        else:
            print()
            break
