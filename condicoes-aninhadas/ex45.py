"""Crie um programa que faça o computador jogar
Jokenpo com voce:
"""
import random
import time
print('='*5, 'JOGO PEDRA PAPEL E TESOURA', '='*5)
print('Escolha uma opção:\n 1 - Pedra \n 2 - Papel \n 3 - Tesoura')
print('-'*10)
escolha = int(input('Digite sua escolha: '))
time.sleep(2)
print('Aguarde...')
time.sleep(2)
pc = random.randrange(0,3)
if escolha == 1 and pc == 3 or escolha == 2 and pc == 1:
    print('Parabéns você ganhou')
elif escolha > 3:
    print('Não disponivel. Escolha dentre as opções listadas acima')
else: 
    print('Você perdeu')

