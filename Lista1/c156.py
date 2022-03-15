from sys import stdin
from collections import Counter

contadorPalavras = Counter()
palavras = []
result = []

def organizadorPalavras(linha):
  for p in linha.split():
    pOrdenada = "".join(sorted(p.upper()))
    if len(p) >= 1:
      contadorPalavras[pOrdenada] += 1
    palavras.append((p, pOrdenada))

while True:
  linha = stdin.readline().strip()
  if linha == "#":
    break
  pOrdenada = organizadorPalavras(linha)

for p, pOrdenada in palavras:
  if not pOrdenada in contadorPalavras or contadorPalavras[pOrdenada] < 2:
    result.append(p)

result.sort()
for p in result:
  print(p)
    
