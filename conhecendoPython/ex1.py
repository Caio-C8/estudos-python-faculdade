# 1 - A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade de broas a cada dia.
# Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50.
# Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos),
# e quanto deve guardar numa conta de poupança (10% do total arrecadado).
# Você foi contratado para fazer os cálculos para o dono.
# Com base nestes fatos, faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados solicitados.


def calcularLucro(qtdePao, qtdeBroa):
    lucro = (qtdePao * 0.12) + (qtdeBroa * 1.5)
    poupanca = lucro * 0.1
    return f"Lucro obtido: R$ {lucro:.2f}\nValor para guardar na poupança: R$ {poupanca:.2f}"


qtdePao = int(input("Quantidade vendida de pães: "))
qtdeBroa = int(input("Quantidade vendida de broas: "))

print(calcularLucro(qtdePao, qtdeBroa))
