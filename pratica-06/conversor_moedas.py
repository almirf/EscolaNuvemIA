import requests
from datetime import datetime

def obter_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/last/{moeda}-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status() # é um método da biblioteca requests que verifica se houve erro na requisição HTTP
        dados = response.json()
        cotacao = dados[f"{moeda}BRL"] ###

        return f"""
        Moeda: {moeda} para BRL
        Valor: R$ {float(cotacao['bid']):.2f}
        Máxima: R$ {float(cotacao['high']):.2f}
        Mínima: R$ {float(cotacao['low']):.2f}
        Data/Hora: {datetime.fromtimestamp(int(cotacao['timestamp']))}
        """
    except requests.RequestException as e:
        return f"Erro ao obter a cotação: {e}"
    except KeyError:
        return f"Moeda não suportada ou não encontrada."
    

moeda = input("Digite o código da moeda para cotação (ex. USD, EUR, GBP): ").upper()
print("\nObtendo sua cotação...")
resultado = obter_cotacao(moeda)
print(resultado)