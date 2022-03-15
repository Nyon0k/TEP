qtd = int(input())
count = 0
ns = []
qtdTestes = []

while count < qtd:
    num = input()
    flag = 0
    contador = 0
    while flag != 1:
        if str(num) == "".join(reversed(num)):
            flag = 1
            break
        else:
            contador = contador+1
            inverso = ''.join(reversed(num))
            resultado = int(num) + int(inverso)
            num = str(resultado)
    ns.append(resultado)
    qtdTestes.append(contador)
    count = count+1

for i in range(qtd):
    print(qtdTestes[i], ns[i])
