"""
Melhore o jogo do Desafio 028 (adivinhar um numero) onde o computador vai 'pensar' em um numero de 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
"""

# from random import *
# r = randint(0,10)
# c = 0
# num = int(input('Digite um numero de 0 a 10: '))
# while num != r:
    
#     num = int(input('Você não acertou, digite novamente: '))
#     c = c + 1
# print('Acertou. Você tentou {} vezes para acertar'.format(c))

from random import randint
computador = randint(0, 10)
acertou = False
palpites = 0
print('Pensei em um numero, consegue adivinhar ?')
while not acertou:
    jogador = int(input('Digite seu palpite: '))
    palpites = palpites + 1
    if jogador == computador:
        acertou = True
    else:
        if jogador <= computador:
            print('Mais... Tente mais uma vez')
        elif jogador > computador:
            print('Menos... Tente mais uma vez')
print('Acertou. Você tentou {} vezes'.format(palpites))