import requests
import json

print('-='*15)
print('Sistema de Conversão de Moeda BRL')
print('-='*15)
valor = float(input('Digite o valor em R$ que deseja converter: '))
print('Opções de Moeda Disponivel')
print('[0] AUD\n'
      '[1] EUR\n'
      '[2] PYG\n'
      '[3] USD\n'
      '[4] CAD\n')
seleciona_moeda = int(input('Digite a opção de moeda que deseja converter: '))
moedas = ['AUD', 'EUR', 'PYG', 'USD', 'CAD']
siglas = ['AUDBRL', 'EURBRL', 'PYGBRL', 'USDBRL', 'CADBRL']
request = requests.get(f'https://economia.awesomeapi.com.br/json/last/{moedas[seleciona_moeda]}')
todos = json.loads(request.content)
atividade = todos[siglas[seleciona_moeda]]
calculo = valor / float(atividade["high"])
print(f'Moeda: {atividade["code"]}\n'
      f'Maior Preço: {float(atividade["high"]):.2f}\n'
      f'Menor Preço: {float(atividade["low"]):.2f}\n'
      f'Valor convertido do Real -> {moedas[seleciona_moeda]}: {calculo:.2f}\n'
      f'Data de Atualização: {atividade["create_date"]}\n')
