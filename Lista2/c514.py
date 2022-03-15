from sys import stdin
for linha_principal in stdin:
    n = int(linha_principal)
    if n == 0:
        break
    lista_padrao = list(range(1, n+1))
    for linha in stdin:
        if linha.rstrip() == '0':
            print()
            break
        
        linha = list(map(int, linha.split()))
        base = []
        cont = 0
        i = 0
        while cont < n:
            base.append(lista_padrao[cont])
            cont += 1
            while len(base) != 0 and linha[i] == base[-1]:
                base.pop()
                i += 1
        if len(base) == 0:
            print('Yes')
        else:
            print('No')
