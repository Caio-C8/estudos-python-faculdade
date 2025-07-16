# O jovem Boris começou a trabalhar em uma lanchonete. A lanchonete é conhecida por fazer um suco de
# laranja com a quantidade certa de açúcar. Como existem diversas jarras na lanchonete, o proprietário
# criou uma medida que para cada 10 ml de líquido deve ser colocada uma colher de açúcar. Implementar
# um algoritmo recursivo capaz de receber a quantidade de ml da jarra e retorna a quantidade de colher de açúcar
# que devem ser utilizadas. Sabendo que a quantidade de ml da jarra é sempre múltipla de 10.


def qtdeAcucar(ml):
    if ml == 10:
        return 1
    else:
        return 1 + qtdeAcucar(ml - 10)


ml = int(input("quantidade de ml da jarra: "))

print(f"{qtdeAcucar(ml)} colheres de açucar.")
