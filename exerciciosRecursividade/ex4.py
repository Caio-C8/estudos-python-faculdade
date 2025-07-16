# Calcula a potência de n elevado a m


def pot(n, m):
    if m == 1:
        return n
    else:
        return n * pot(n, m - 1)


print(pot(2, 3))
