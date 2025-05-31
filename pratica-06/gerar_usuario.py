import requests

def gerar_usuario():
    url = "https://randomuser.me/api/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['first']} {dados['name']['last']}"
        pais = dados['location']['country']
        email = dados['email']
        return f'Nome: {nome}\n E-mail: {email} \n País: {pais}'

    except requests.RequestException:
        return f'Erro ao obter uruário.'
    
print("Gerando um usuario aleatorio......")
usuario = gerar_usuario() 
print(usuario)
