# Calcula o produto de x vezes n


def mult(x, n):
    if n == 1:
        return x
    else:
        return x + mult(x, n - 1)


print(mult(5, 20))
