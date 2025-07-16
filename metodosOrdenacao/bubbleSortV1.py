def bubbleSort(lista):
    lista_tam = len(lista)
    for i in range(lista_tam):
        for j in range(0, lista_tam - i - 1):
            if lista[j] > lista[j + 1]:
                temp = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = temp
                # lista[j], lista[j + 1] = lista[j + 1], lista[j]

    return lista


lista = [50, 60, 40, 30, 20, 70, 17, 8]
print("Lista original:", lista)

lista_ordenada = bubbleSort(lista)
print("Lista ordenada:", lista_ordenada)
