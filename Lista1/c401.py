from sys import stdin

def testPalindromo(p):
    if not p == p[::-1]:
        return False
    return True

def testEspelhado(p, tam):
    for i in range(tam):
        if letrasInvertidas.get(p[i], 0) != p[len(p)-i-1]:
            return False
    return True

def result(p, palindromo, espelhado):
    if not palindromo and not espelhado:
        print(p + " -- is not a palindrome.\n")

    elif palindromo and not espelhado:
        print(p + " -- is a regular palindrome.\n")

    elif not palindromo and espelhado:
        print(p + " -- is a mirrored string.\n")

    else:
        print(p + " -- is a mirrored palindrome.\n")
    

letrasInvertidas = {'A':'A', 'E':'3', 'H':'H', 'I':'I',
                    'J':'L', 'L':'J', 'M':'M', 'O':'O',
                    'S':'2', 'T':'T', 'U':'U', 'V':'V',
                    'W':'W', 'X':'X', 'Y':'Y', 'Z':'5',
                    '1':'1', '2':'S', '3':'E', '5':'Z',
                    '8':'8'}

for p in stdin:
    p = p.rstrip()
    tam = (len(p)//2)+1
    palindromo = testPalindromo(p)
    espelhado = testEspelhado(p, tam)
    result(p, palindromo, espelhado)
    
