"""
Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

- Distância percorrida: 300 km
- Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
distancia_percorrida = 300 # em quilometros (km)
combustivel_gasto = 25 # em litros
consumo_medio = distancia_percorrida / combustivel_gasto
print("Dados da Viagem:")
print(f"Distância percorrida: {distancia_percorrida} quilômetros (km)")
print(f"Combustível gasto: {combustivel_gasto} litros (1)")
print ("Consumo médio: ", round (consumo_medio, 2), "km/1")
#print(consumo_medio)

