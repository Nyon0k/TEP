from sys import stdin

qtd = int(stdin.readline().strip())
limit = range(qtd)

for c in limit:
    linha = stdin.readline().strip().strip()
    pilha = []
    correto = True
    for ch in linha:
        if ch in "[(":
            pilha.append(ch)
        elif ch in "])":
            if len(pilha) == 0:
                correto = False
                break
            anterior = pilha.pop()
            if ch == ")" and anterior != "(":
                correto = False
                break
            if ch == "]" and anterior != "[":
                correto = False
                break
    if len(pilha) == 0 and correto is True:
        print("Yes")
    else:
        print("No")
