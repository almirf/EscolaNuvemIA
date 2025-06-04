import csv

def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerow(['Nome', 'Idade', 'Cidade'])
        escritor.writerows(dados) ## várias linhas
    print(f"Dados salvos em {nome_arquivo}")


dados = [
    ['Ana', 28, 'Rio de Janeiro'],
    ['Bruno', 25, 'São Paulo'],
    ['Carlos', 33, 'Belo Horizonte'],
    ['Daniel', 25, 'Vitória']
]

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo CSV: ").strip()
    escrever_csv(nome_arquivo, dados)