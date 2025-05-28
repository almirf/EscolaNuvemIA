def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:

    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

total_conta = float(input('Insira o valor total da conta: R$'))
porcentagem = float(input('Insira a porcentagem da gorjeta (%)'))

gorjeta = calcular_gorjeta(total_conta, porcentagem)
print(f'Para uma conta no total de R${total_conta:.2f}, a gorjeta de {porcentagem}% é R${gorjeta:.2f}')
100