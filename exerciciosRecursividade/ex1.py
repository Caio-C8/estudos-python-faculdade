# Calcula a soma dos números naturais de 1 a n.


def somaNat(n):
    if n == 1:
        return 1
    else:
        return n + somaNat(n - 1)


print(somaNat(5))
