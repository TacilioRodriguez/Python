"""
Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar.
No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
"""

custa = 0
total = 0
while True:
    produto = str(input('Digite o nome do Produto: '))
    preco = float(input('Digite o Preço [R$]: '))
    total = total + preco
    continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if preco > 1000:
        custa = custa + 1
    if continuar == 'N':
        break
print(f'O Total gasto na compra foi de R$ {total:.2f} -  {custa} Custam mais de R$1mil reais')