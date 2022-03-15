from sys import stdin

for linha in stdin:
    n, k = map(int, linha.split())
    if n == 0 and k == 0:
        break
    p = list(range(1, n+1))
    i = 0
    while len(p) > 1:
        i = (i + k - 1) % len(p)
        ik, vk = i, p[i]
        p.remove(vk)
        i = (i + k - 1) % len(p)
        ib, vb = i, p[i]
        if ik < ib:
            p.remove(vb)
            p.insert(ik, vb)
            i = (ik+1)%len(p)
        if ik > ib:
            p.insert(ik, vb)
            p.remove(vb)
            i = (ik)%len(p)
        else:
            i = (ik+1)%len(p)
    print(max(1, (1-p[0])%(n+1)))
