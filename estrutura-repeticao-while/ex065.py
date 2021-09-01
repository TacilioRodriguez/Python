"""
Crie um programa que leia varios numeros inteiros pelo teclado. No final da execução, mostre a media entre todos os
valores e qual foi a maior e o menor valor lidos. O programa deve perguntar ao usuario se ele quer ou não continuar
a digitar valores
"""
import time
r = ''
cont = 0
maior = 1
menor = 0
soma = 0
while r != 'N':
    num = int(input('Digite um numero: '))
    r = str(input('Quer continuar digitando [S/N]: ')).upper()
    cont = cont + 1
    soma = num + soma
    media = soma / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num
print('Finalizando .. ')
time.sleep(2)
print('~~'*30)
print('Foram digitados {} valores.\nA media entre eles foi {:.2f} e a soma {}.\nMaior numero {} e menor numero {}'.format(cont, media, soma, maior, menor))
print('~~'*30)