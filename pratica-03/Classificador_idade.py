"""
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).
"""
idade = int(input("Digite sua idade: "))

# Classifica de acordo com a faixa etária
if 0 <= idade <= 12:
    categoria = "Criança"
elif 13 <= idade <= 17:
    categoria = "Adolescente"
elif 18 <= idade <= 59:
    categoria = "Adulto"
elif idade >= 60:
    categoria = "Idoso"
else:
    categoria = "Idade inválida"

# Exibe o resultado
print(f"Categoria: {categoria}")