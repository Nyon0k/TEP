def calc(tam, num):
    if tam == n:
        if num == b1:
            return True;
        return False
    for i in range(m):
        if esc[i]:
            continue
        if arr1[i] == num or arr2[i] == num:
            esc[i] = 1
            flag = False
            if arr1[i] == num:
                flag = calc(tam+1, arr2[i])
            else:
                flag = calc(tam+1, arr1[i])
            if flag == True:
                return True
            esc[i] = 0
    return False

while True:
    n = int(input())
    if n == 0:
        break
    m = int(input())
    esc = []
    arr1, arr2 = [], []
    a1, a2 = list(map(int, input().split()))
    b1, b2 = list(map(int, input().split()))
    for _ in range(m):
        a, b = list(map(int, input().split()))
        arr1.append(a)
        arr2.append(b)
        esc.append(0)
    res = calc(0, a2)
    if res:
        print('YES')
    else:
        print('NO')
