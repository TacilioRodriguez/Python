"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas ja são maiores (21 anos)
"""

from datetime import date
atual = date.today().year
maioridade = 0
menoridade = 0
for nas in range(1,8):
    nasc = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(nas)))
    idade = atual - nasc
    if idade >= 21:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print('Ao todo tivemos {} maiores de idade e\n{} pessoas menores de idade'.format(maioridade, menoridade))
