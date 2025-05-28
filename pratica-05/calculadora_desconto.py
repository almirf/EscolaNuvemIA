def calcular_desconto(preco: float, percentual_desconto: float) -> float:
    
    desconto = preco * (percentual_desconto / 100)
    preco_final = preco - desconto
    return preco_final

preco_original = float(input('Digite o preço do produto: R$'))
desconto = float(input('Digite o percentual do desconto: '))

preco_com_desconto = calcular_desconto(preco_original, desconto)

print(f"Preço final com {desconto}% de desconto é: R$ {preco_com_desconto:.2f}")