def is_palindromo(texto):
    #Remover espaços e converte para minúsculas
    texto_limpo = ''.join(char.lower()
                          for char in texto
                          if char.isalnum())
    
    return texto_limpo == texto_limpo[::-1]
    

expressao = input('Insira uma expressão para verificação: ')
resultado = is_palindromo(expressao)

if resultado == True:
    resposta = 'SIM'

else:
    resposta = 'NÃO'

print(f'A expressão {expressao} é um palindromo? {resposta}')
