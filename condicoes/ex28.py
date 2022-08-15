#Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5 
# e peça para o usuário descobrir qual foi o numero escolhido pelo computador. 
# O programa devera escrever na tela se o usuário venceu ou perdeu.

from random import *

r = randrange(0,5)
digite = int(input('Digite um numero de 0 a 5: '))
if r == digite:
    print("Você acertou!! Parabéns")
elif digite >5:
    print("O Numero digitado é maior do que 5. Não é permitido")
else:
    print('Você não acertou. Tente novamente')

