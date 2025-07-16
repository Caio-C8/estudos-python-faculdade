def mergeSort(lista):
    if len(lista) <= 1:
        return lista

    meio = len(lista) // 2
    esquerda = mergeSort(lista[:meio])
    direita = mergeSort(lista[meio:])

    return merge(esquerda, direita)


def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])

    return resultado


lista = [30, 27, 58, 29, 17, 60, 70, 80, 21]
print("Lista original:", lista)

lista_ordenada = mergeSort(lista)
print("Lista ordenada:", lista_ordenada)
