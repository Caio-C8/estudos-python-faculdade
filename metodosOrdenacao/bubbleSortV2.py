def bubbleSort(lista):
    n = len(lista)
    for i in range(n):
        trocou = False

        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:

                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                trocou = True

        if not trocou:
            break

    return lista


lista = [50, 60, 40, 30, 20, 70, 17, 8]
print("Lista original:", lista)

lista_ordenada = bubbleSort(lista)
print("Lista ordenada:", lista_ordenada)
