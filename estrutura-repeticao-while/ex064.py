"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai parar
quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos
numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag 999).
"""


cont = 0
soma = 0
numero = 0
while numero != 999:
    numero = int(input('Digite um numero ou [999 para parar]: '))
    soma = soma + numero
    if numero != 999:
        cont = cont + 1
print('Foram digitados {} numero e a soma é {}'.format(cont, soma - 999))