from itertools import permutations

n = int(input())
for _ in range(n):
    linha = input()
    res = sorted(''.join(chars) for chars in permutations(linha, len(linha)))
    if res[0] == res[-1]:
        print(linha+'\n')
        continue
    for i in range(len(res)):
        if res[i] != res[i-1]:
            print(res[i])
    print()
