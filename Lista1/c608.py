from sys import stdin

limit = 3

n = int(stdin.readline())
if n < 1:
    "Erro"
else:
    c = 0
    while c < n:
        letras = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
        leve = letras
        pesado = letras
        cont = 0
        while cont < limit:
            esq, direita, peso = stdin.readline().split()
            esq, direita = set(esq), set(direita)

            if peso == 'even':
                leve = leve - (esq | direita)
                pesado = pesado - (esq | direita)

            if peso == 'up':
                leve = leve.intersection(direita)
                pesado = pesado.intersection(esq)

            if peso == 'down':
                leve = leve.intersection(esq)
                pesado = pesado.intersection(direita)
        
            cont += 1
        if leve > pesado:
            print(leve.pop(), "is the counterfeit coin and it is light.")
        else:
            print(pesado.pop(), "is the counterfeit coin and it is heavy.")
    
        c += 1
