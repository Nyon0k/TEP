linha = input().split()
term1 = linha[0]
term2 = linha[1]

while not(term1 == '0' and term2 == '0'):
    t1 = int(term1)
    t2 = int(term2)
    charsT1 = []
    charsT2 = []
    tamT1 = len(term1)
    tamT2 = len(term2)
    somador = 0
    if tamT1 > tamT2:
        qtdZeros = tamT1-tamT2
        cont = 0
        while cont < qtdZeros:
            charsT2.append('0')
            cont += 1
    if tamT1 < tamT2:
        qtdZeros = tamT2-tamT1
        cont = 0
        while cont < qtdZeros:
            charsT1.append('0')
            cont += 1
    #print(tamT1,tamT2)
    for c in term1:
        charsT1.append(c)
    for c in term2:
        charsT2.append(c)
    anterior = 0
    #print('len(charsT1)',len(charsT1))
    for index in range(len(charsT1)-1,-1,-1):
        #print('index',index)
        #print(charsT1[index], charsT2[index])
        #print('anterior',anterior)
        if len(str(anterior)) > 1:
            anterior == anterior[0]
            #print('anterior[0]',anterior[0])
            soma = int(charsT1[index])+int(charsT2[index])+int(anterior[0])
        else:
            soma = int(charsT1[index])+int(charsT2[index])
        #print('soma',soma)
        if soma >= 10:
            anterior = str(soma)
            somador += 1
            #print('flag')
        else:
            anterior = str(soma)
    #print(len(charsT1),len(charsT2))
    #print(charsT1,charsT2)
    if somador == 0:
        print('No carry operation.')
    if somador == 1:
        print('1 carry operation.')
    if somador > 1:
        print(str(somador)+' carry operations.')
    linha = input().split()
    term1 = linha[0]
    term2 = linha[1]
