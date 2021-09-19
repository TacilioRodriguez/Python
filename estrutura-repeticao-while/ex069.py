"""
Crie um programa que leia a idade e o sexo de varias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuario quer ou nao continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos
B) quantos homens foram cadastrados
C) quantas mulheres tem mais de 20 anos

Colocar validação para digitação errada nas opções de pergunta.
"""

M = 0
maiores18 = 0
F = 0
prosseguir = ' '
while True:
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MFmf:':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        maiores18 = maiores18 + 1
    if sexo == 'M':
        M = M + 1
    if idade > 20 and sexo == 'F':
        F = F + 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Tem {maiores18} mais de 18 anos. Foram cadastrados {M} Homens, e existem {F} mulheres com mais de 20 anos ')



