"""
Desenvolva um programa que leia o nome, idade e sexo de
4 pessoas. No final do programa, mostre:

- A Media de idade do grupo
- Qual é o nome do homem mais velho
- Quantas mulheres tem menos de 20 anos
"""
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = ''
mulhervinte = 0
for p in range (1,3):
    print('----- Pessoa {}ª -----'.format(p))
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhervinte = mulhervinte + 1
mediaidade = somaidade / 4 
print('A Media de idade do grupo é {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelho))
print('São {} mulheres menores de 20 anos'.format(mulhervinte))