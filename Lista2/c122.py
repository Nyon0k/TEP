from sys import stdin
from collections import OrderedDict

def cria_arv(dic):
    aux = sorted(dic.items(), key=lambda x: (len(x[0]), x[0]))
    dic_ordenado = OrderedDict(aux)
    res = ''
    for chave, valor in dic_ordenado.items():
        if dic_ordenado.get(chave[:-1], 0) != 0:
            res += valor+' '
        else:
            res = 'not complete'
            break
    print(res.rstrip())

dic = {}
create = False
nc = False

for linha in stdin:
    linha = linha.split()
    if len(linha[-1]) == 2:
        linha.pop()
        create = True
    for node in linha:
        node = tuple(map(str, node[1:-1].split(',')))
        if dic.get(node[1], 0) == 0:
            dic[node[1]] = node[0]
        else:
            nc = True
    if create:
        if nc:
            print('not complete')
        else:
            cria_arv(dic)
        dic = {}
        create = False
        nc = False
