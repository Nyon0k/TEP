from sys import stdin

for linha in stdin:
    linha = linha.rstrip()
    cont = 1
    div = []
    tam = len(linha)
    while cont <= (tam//2)+1:
        if (tam%cont == 0):
            div.append(cont)
        cont += 1
    div.append(tam)
    div_res = div
    unique = True
    if linha == '.':
        break
    for i in div_res:
        power = tam//i
        achou = True
        for j in range(power):
            if linha[:i] != linha[j*i:j*i+i]:
                achou = False
                break
        if achou:
            break
    print(power)
