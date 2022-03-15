from sys import stdin

for entrada in stdin:
  linha = entrada.split()
  f = int(linha[0])
  c = int(linha[1])
  f1 = f
  c1 = c

  if f == 0 or c == 0:
    break
  if f > c:
    f, c = c, f
  if f == 1:
    qtdCavaleiros = c
  elif f == 2:
    if 2 < c%4:
      multiplicador = 2
    else:
      multiplicador = c%4
    qtdCavaleiros = 4*(c//4)+2*multiplicador
  else:
    qtdCavaleiros = (c*f+1)/2
  print(str(int(qtdCavaleiros)) + " knights may be placed on a " + str(f1) + " row " + str(c1) + " column board.")
