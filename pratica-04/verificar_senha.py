while True:
    senha = input("Digite a senha ou 'sair' para encerrar: ")
            
    if senha.lower() == "sair":
       print("o programa foi encerrado.")
       break
           
    if len(senha) <8 :
       print("Senha Fraca. a senha precisa ter pelo menos 8 caracteres.")
       continue
                        
    if not any (caractere.isdigit() for caractere in senha):
       print("Senha Fraca. a senha precisa ter pelo menos 1 numero.")
       continue

    if not any (caractere.isalpha() for caractere in senha):
       print("Senha Fraca. a senha precisa ter pelo menos 1 letra.")
       continue

    print("senha forte")
    break