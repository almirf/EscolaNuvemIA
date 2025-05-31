import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "CEP inválido"
        return f"""
        CEP: {dados ["cep"]}
        logradouro: {dados["logradouro"]}
        bairro: {dados["bairro"]}
        cidade: {dados["localidade"]}
        estado: {dados["uf"]}
        """
    except requests.RequestException as e:
        return f"Erro na consulta {e}"

cep = input("Digite um CEP para consulta (apenas nuémeros): ")
print("Consultando CEP...")
resultado = consulta_cep(cep)
print(resultado)