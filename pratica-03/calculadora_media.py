# Lê as quatro notas com uma casa decimal
#n1, n2, n3, n4 = map(float, input("Digite as quatro notas separadas por espaço: ").split())

n1 = float(input("Digite a 1a Nota: "))
n2 = float(input("Digite a 2a Nota: "))
n3 = float(input("Digite a 3a Nota: "))
n4 = float(input("Digite a 4a Nota: "))

# Calcula a média ponderada
media = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10

# Exibe a média com uma casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7.0:
    print("Aluno aprovado.")
elif media < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    nota_exame = float(input("Digite a nota do exame: "))
    print(f"Nota do exame: {nota_exame:.1f}")
    media_final = (media + nota_exame) / 2
    if media_final >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")