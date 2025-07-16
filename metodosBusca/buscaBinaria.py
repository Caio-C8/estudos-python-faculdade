def buscaBin(lista, item):
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if item == lista[meio]:
            return meio
        elif item > lista[meio]:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


lista = [4, 9, 11, 12, 15, 30, 42, 51, 67, 80, 81, 90, 97, 102]
item = 30

resultado = buscaBin(lista, item)

if resultado == -1:
    print(f"Valor {item} não encontrado.")
else:
    print(f"Valor {item} encontrado no índice {resultado}.")
