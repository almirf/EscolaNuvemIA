pares = 0
impares = 0

while True:
        entrada = input("Digite um numero inteiro ou 'fim' para encerrar  ")
        if entrada.lower() == 'fim':
           break

        try:
           numero = int(entrada)            
           if numero % 2 == 0:
               print(f"o número {numero} é par.")
               pares +=1 # "é a mesma coisa, mas de outra forma. pares = pares + 1")               
           else:
               print(f"o numero {numero} é impar")   
               impares += 1
        except ValueError:      
            print("Erro encontrado. Por favor , insira um número inteiro.")
            continue
        
print("\n Resultado Final:") 
print(f"A quantidade de némeros pares é: {pares}")        
print(f"A quantidade de números ímpares é: {impares}")
