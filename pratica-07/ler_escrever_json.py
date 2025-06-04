import json

def ler_json(nome_arquivo):
    try:    
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json: ## utf por uft
            dados = json.load(arquivo_json)
            print(dados)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def escrever_json(nome_arquivo, dados):
    try:    
        with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json: ## utf por uft   ==> 'w'
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        print(f"Dados salvos em {nome_arquivo}")
    except FileNotFoundError as e:
        print("Erro ao salvar o arquivo {e}")    ## f strings  

dados = {
    "nome": "Ana",
    "idade": 30,
    "cidade": "São Paulo"
}        

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo JSON: ").strip()
    escrever_json(nome_arquivo, dados)
    ler_json(nome_arquivo)