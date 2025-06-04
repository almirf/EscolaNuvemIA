import pandas as pd

def processar_logs_treinamento(nome_arquivo):
    try:
        df = pd.read_csv(nome_arquivo)
        media_tempo = df['tempo_execucao'].mean()
        desvio_padrao_tempo = df['tempo_execucao'].std()
        print(f"A média de tempo de execução é: {media_tempo:.2f} segundos.")
        print(f"O desvio padrão é: {desvio_padrao_tempo:.2f}.")
    except FileNotFoundError:
        print("O arquivo que você digitou não foi encontrado.")    
    except Exception as e:
        print(f"O erro ao processar o arquivo solicitado é: {e}")    


nome_arquivo = input("Digite o nome do arquivo de log: ")

processar_logs_treinamento(nome_arquivo)