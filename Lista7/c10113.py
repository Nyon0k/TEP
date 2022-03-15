from fractions import Fraction
tree = dict()


def search(root, target):
    path = []
    visited = []
    stack = [root]

    while stack:
        node = stack.pop()
        if node not in visited:
            path.append(node)
            if node == target:
                return path
            visited.append(node)
            stack.extend(tree[node])


def calculate_exchange(path):
    acc = 1
    for i in range(len(path[:-1])):
        acc *= tree[path[i]][path[i+1]]
    return acc


while True:
    line = input()
    if line == '.':
        break
    else:
        line = line.split()
        if line[0] == '!':
            if line[2] not in tree:
                tree[line[2]] = dict()
            if line[5] not in tree:
                tree[line[5]] = dict()

            tree[line[2]][line[5]] = Fraction(int(line[4]), int(line[1]))
            tree[line[5]][line[2]] = Fraction(int(line[1]), int(line[4]))
        else:
            path = search(line[1], line[3])
            if path != None:
                exchange = calculate_exchange(path)
                print(exchange.denominator, line[1],
                      "=", exchange.numerator, line[3])
            else:
                print("?", line[1], "= ?", line[3])
