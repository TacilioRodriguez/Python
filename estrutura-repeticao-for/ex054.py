"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas ja são maiores (21 anos)
"""

for nas in range(0,3):
    n = int(input('Digite o ano de nascimento: '))
    maior = 2021 - n
if maior >= 21:
    m = 'Maior'
    print("{} são maiores de idade".format(m.count('Maior')))
else:
    n = 'Menor'
    print('{} são menores de idade'.format(n.count('Menor')))

