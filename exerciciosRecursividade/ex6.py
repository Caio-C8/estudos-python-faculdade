# Verifica se uma palavra é um palíndromo, ou seja, se ela é lida/escrita da mesma forma da direita para esquerda ou vice-versa


def palindromo(p):
    if len(p) <= 1:
        return True
    elif p[0] == p[-1]:
        return palindromo(p[1:-1])
    else:
        return False


print(palindromo("radar"))
