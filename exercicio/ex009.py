# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar, considere 1 USD = 3.27

dinheiro = float(input('Quanto voce tem na carteira? R$ '))
cotacao = float(input('Qual a cotação do dolar hoje? US$ '))
dolar = dinheiro/cotacao
print('Com R${:.2f}, considerando a cotação do dolar hoje, você pode comprar US${:.2f}'.format(dinheiro,dolar))