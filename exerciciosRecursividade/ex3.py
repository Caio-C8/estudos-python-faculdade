# Calcula o fatorial de um número n


def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)


print(fatorial(5))
