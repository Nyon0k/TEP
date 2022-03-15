entradas = int(input())
rosa_dos_ventos = ['N', 'E', 'S', 'W']
array = [[-1, 0], [0, 1], [1, 0], [0, -1]]
for l in range(entradas):
    input()
    qtd_linhas, qtd_colunas = input().split()
    maze = []
    for linha in range(int(qtd_linhas)):
        maze.append(list(input()))
    
    pos_x, pos_y = list(map(int, input().split()))
    direcao = 0
    
    movimentos = []
    while True:
        texto = list(input())
        for char in texto:
            if char != ' ':
                movimentos.append(char)
        if movimentos[-1] == 'Q':
            break

    for char in movimentos:
        if char == 'Q':
            break
        if char == 'R':
            direcao = (direcao+1)%4
        if char == 'L':
            direcao = (direcao+3)%4
        if char == 'F':
            x_atual = pos_x-1+array[direcao][0]
            y_atual = pos_y-1+array[direcao][1]
            if maze[x_atual][y_atual] == ' ':
                pos_x = x_atual+1
                pos_y = y_atual+1

    print(pos_x, pos_y, rosa_dos_ventos[direcao])
    if l != entradas-1:
        print()
