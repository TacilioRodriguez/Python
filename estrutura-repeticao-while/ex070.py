"""
Crie um programa que leia o nome e o preço de varios produtos. O programa devera perguntar se o usuario vai continuar.
No final, mostre:
A) Qual é o total gasto na compra
B) Quantos produtos custam mais de R$1000
C) Qual é o nome do produto mais barato
"""

custa = 0
total = 0
conta = 0
menor = 0
barato = ''
while True:
    produto = str(input('Digite o nome do Produto: '))
    preco = float(input('Digite o Preço [R$]: '))
    total = total + preco
    conta = conta + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja Continuar [S/N]: ')).strip().upper()[0]
    if conta == 1:
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    if preco > 1000:
        custa = custa + 1
    if continuar == 'N':
        break
print(f'O Total gasto na compra foi de R$ {total:.2f} -  {custa} Produto Custa mais de R$ 1mil reais \n O produto mais barato foi {barato} que custa R${menor:.2f}')