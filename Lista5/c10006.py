def verifica_primo(num):
    if num <= 3:
        return True
    if num%2 == 0 or num%3 == 0:
        return False
    c = 5
    while c**2 <= num:
        if num%c == 0 or num%(c+2) == 0:
            return False
        c = c+6
    return True

entrada = int(input())
while entrada != 0:
    carmichael = True
    if verifica_primo(entrada):
        result = (str(entrada)+' is normal.')
        print(result)
        entrada = int(input())
        continue
    for i in range(2, entrada):
        if i != pow(i, entrada, entrada):
            result = (str(entrada)+' is normal.')
            print(result)
            carmichael = False
            break
    if carmichael == True:
        print('The number '+str(entrada)+' is a Carmichael number.')
    entrada = int(input())
