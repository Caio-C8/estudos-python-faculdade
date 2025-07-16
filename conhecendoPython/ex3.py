# 3 - Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar (em relação ao ano de 2024).
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.


def verificarAlistamento(ano):
    if ano > 2006 and ano <= 2024:
        falta = ano - 2006
        return f"Você tem menos de 18 anos, faltam {falta} ano(s) para fazer o alistamento."
    elif ano < 2006:
        anoIdade18 = ano + 18
        sobra = 2024 - anoIdade18
        return f"Você tem mais de 18 anos, o alistamento deveria ter sido feito há {sobra} anos atrás."
    elif ano == 2006:
        return "Pode se alistar."
    else:
        return "Data inválida."


ano = int(input("Ano de nascimento: "))

print(verificarAlistamento(ano))
