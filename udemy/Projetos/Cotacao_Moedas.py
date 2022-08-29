
# essa linha importa os recursos
import requests, json
import pandas as pd
from pandas import json_normalize

# essa linha pega os recursos do link e atribui a variavel

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')

# realiza a conversão do response para um formato acessível ao python
json_data = json.loads(response.text)

df = json_normalize(json_data['USDBRL'])



df = df.astype({'high':'float','low':'float','low':'float','bid':'float','ask':'float'}).round(2)


# pd.to_numeric(formatters={'high':'${:,.2f}'.format})
# df.astype(float('high')).round(3)
file_name = 'Cotacao_Moedas'
df.to_csv(rf'C:\Users\tacilio.pereira\Desktop\Python\SaveFiles\{file_name}.csv', sep=';', encoding='utf-8-sig',index=None, header=True)
print('Arquivo Salvo com Sucesso')