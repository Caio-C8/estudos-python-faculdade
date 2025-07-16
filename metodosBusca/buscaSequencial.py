def buscaSeq(lista, item):
    # indice se refere a posição da lista. elemento se refere ao conteúdo da posição.
    # O indice começa em 0 e itera até acabar as posições da lista, nesse caso até 13.
    for indice, elemento in enumerate(lista):
        if elemento == item:
            return indice

    return -1


lista = [4, 9, 12, 11, 15, 30, 42, 51, 67, 80, 81, 90, 97, 102]
item = 30

resultado = buscaSeq(lista, item)

if resultado == -1:
    print(f"Valor {item} não encontrado.")
else:
    print(f"Valor {item} encontrado no índice {resultado}.")
