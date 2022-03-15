n = int(input())

for _ in range(n):
    entradas = int(input())
    valores = set()
    anterior, atual, res = 0, 0, 0

    snow = [input() for _ in range(entradas)]
        
    while atual < entradas:
        if snow[atual] not in valores:
            valores.add(snow[atual])
            res = max(res, atual-anterior+1)
        else:
            while anterior < atual and snow[anterior] != snow[atual]:
                valores.remove(snow[anterior])
                anterior += 1
            anterior += 1
        atual += 1
    print(res)
