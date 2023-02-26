import requests
import json
from time import sleep

cep = str(input('Digite o CEP: '))
if len(cep) < 8 or len(cep) > 8:
    while True:
        print(f'Voce digitou somente {len(cep)} numeros, precisa ser 8 digitos.')
        cep = str(input('Por favor, digite o CEP novamente: '))
        if len(cep) == 8:
            break
request = requests.get(f"https://brasilapi.com.br/api/cep/v2/{cep}")
arquivo = json.loads(request.content)
print('Consultando o CEP...')
sleep(0.8)
print('Carregando as Informações...')
sleep(0.3)
print('-='*20)
print('=-INFORMAÇÕES DO CEP DIGITADO-=')
print(f'CEP: {arquivo["cep"]}\n'
      f'Estado: {arquivo["state"]}\n'
      f'Cidade: {arquivo["city"]}\n'
      f'Bairro: {arquivo["neighborhood"]}\n'
      f'Rua: {arquivo["street"]}\n')

