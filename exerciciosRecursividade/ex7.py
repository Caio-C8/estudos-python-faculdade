# Calcula o máximo divisor comum (MDC) entre dois números inteiros a e b


def mdc(a, b):
    if a % b == 0:
        return b
    else:
        return mdc(b, a % b)


print(mdc(48, 18))
