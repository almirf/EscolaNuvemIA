"""
Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

- Nome do produto: "Camiseta"
- Preço original: R$ 50.00
- Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

#Calculadora de desconto de uma loja

#Informações do produto
nome_produto = "Camiseta"
preco_original = 50.00
porcentagem_desconto = 20
valor_desconto = (preco_original * porcentagem_desconto / 100)

#Calculo de Desconto
preco_final = preco_original - valor_desconto

#Exibicao dos Resultados
print("Produto:", nome_produto)
print("Preco Original: R$ {preco_original:.2f}")
print("Desconto:", porcentagem_desconto)
print("Valor do Desconto: R$ {valor_desconto:.2f}")
print("Preco Final: R$ {preco_final:.2f}")
