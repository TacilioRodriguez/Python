"""Faça um programa que leia o ano de nascimento de um jovem e informe, 
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime
import time
nasc = int(input('Digite o seu ano de nascimento: '))
hoje = datetime.datetime.today()
alist = hoje.year - nasc
print('Aguarde...')
time.sleep(2)
print('Processando...')
time.sleep(2)
if alist == 17:
    print('Hora de se Alistar')
elif alist < 17:
    falta =  17 - alist
    print('Você ainda vai se alistar, falta {} anos'.format(falta))
elif alist > 17:
    passou = alist - 17
    print('Já passou {} do tempo do alistamento'.format(passou))

