# 2 - O cardápio de uma lanchonete é o seguinte:
#           Especificação	    Código	    Preço
#           Cachorro quente	    100	         1,20
#           Bauru simples	    101	         1,30
#           Bauru com ovo	    102	         1,50
#           Hambúrger	        103	         1,20
#           Cheeseburguer	    104	         1,30
#           Refrigerante	    105	         1,00
# Escrever um algoritmo que leia o código do item pedido, a quantidade e calcule o valor a ser pago por aquele lanche.
# Considere que a cada execução somente será calculado um item.


def valorPedido(code, qtde):
    if code == "100":
        valor = qtde * 1.2
        return f"Pedido: {qtde} cachorro(s) quente(s)\nValor: R$ {valor:.2f}"
    elif code == "101":
        valor = qtde * 1.3
        return f"Pedido: {qtde} bauru(s) simples\nValor: R$ {valor:.2f}"
    elif code == "102":
        valor = qtde * 1.5
        return f"Pedido: {qtde} bauru(s) com ovo\nValor: R$ {valor:.2f}"
    elif code == "103":
        valor = qtde * 1.2
        return f"Pedido: {qtde} habúrguer(s)\nValor: R$ {valor:.2f}"
    elif code == "104":
        valor = qtde * 1.3
        return f"Pedido: {qtde} cheeseburger(s)\nValor: R$ {valor:.2f}"
    elif code == "105":
        valor = qtde * 1
        return f"Pedido: {qtde} refrigerante(s)\nValor: R$ {valor:.2f}"
    else:
        return "Código inválido."


code = "0"
while (
    code != "100"
    and code != "101"
    and code != "102"
    and code != "103"
    and code != "104"
    and code != "105"
):
    code = input("Código do produto: ")
    qtde = int(input("Quantidade do produto: "))

    print(valorPedido(code, qtde))
