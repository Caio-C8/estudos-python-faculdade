# Calcula a soma de uma sequência de números


def somaDigitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + somaDigitos(n // 10)


print(somaDigitos(1234))
