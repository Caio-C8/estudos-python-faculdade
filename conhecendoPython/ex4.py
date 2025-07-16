# 4 - Implementar um programa capaz de ler a nota de 10 alunos e retornar a quantidade de alunos aprovados,
# considerando que a média para aprovação no mínimo 60,00 pontos.


def verificarNota():
    aprovado = 0
    for i in range(10):
        nota = float(input(f"Nota do aluno {i+1}: "))
        if nota >= 60:
            aprovado = aprovado + 1
        if i == 9:
            return f"{aprovado} alunos aprovados."


print(verificarNota())
