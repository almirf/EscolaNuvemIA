nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor: "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês: "))

# Cálculo da comissão (15%) e do total a receber
comissao = total_vendas * 0.15
total_a_receber = salario_fixo + comissao

# Saída formatada
print(f"TOTAL = R$ {total_a_receber:.2f}")