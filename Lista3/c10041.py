from sys import stdin
from statistics import median

entrada = int(stdin.readline())
for _ in range(entrada):
	linha = stdin.readline()
	linha = list(map(int, linha.split()))
	casa = linha[1:]
	dist = 0
	m = int(median(casa))
	for d in casa:
		dist += abs(d - m)
	print(dist)
