"""
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

C para F: F = (C \* 1.8) + 32
F para C: C = (F - 32) / 1.8
C para K: K = C + 273.15
K para C: C = K - 273.15
F para K: K = (F - 32) / 1.8 + 273.15
K para F: F = (K - 273.15) \* 1.8 + 32
"""

# Funções para conversão
def celsius_para_fahrenheit(c):
    return c * 9/5 + 32

def celsius_para_kelvin(c):
    return c + 273.15

def fahrenheit_para_celsius(f):
    return (f - 32) * 5/9273.15

def fahrenheit_para_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_para_celsius(k):
    return k - 273.15

def kelvin_para_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Entrada do usuário
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C, F ou K): ").upper()
destino = input("Digite a unidade de destino (C, F ou K): ").upper()

# Conversão
if origem == destino:
    resultado = temperatura
elif origem == "C" and destino == "F":
    resultado = celsius_para_fahrenheit(temperatura)
elif origem == "C" and destino == "K":
    resultado = celsius_para_kelvin(temperatura)
elif origem == "F" and destino == "C":
    resultado = fahrenheit_para_celsius(temperatura)
elif origem == "F" and destino == "K":
    resultado = fahrenheit_para_kelvin(temperatura)
elif origem == "K" and destino == "C":
    resultado = kelvin_para_celsius(temperatura)
elif origem == "K" and destino == "F":
    resultado = kelvin_para_fahrenheit(temperatura)
else:
    print("Unidade inválida.")
    exit()

# Exibição do resultado
print(f"{temperatura}°{origem} é igual a {resultado:.2f}°{destino}")