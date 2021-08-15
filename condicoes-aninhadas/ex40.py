"""Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma mensagem no final, de acordo com a media atingida:
- Média abaixo de 5.0:
    Reprovado
- Média entre 5,0 e 6,9:
    Recuperação
-Média 7 ou superior:
    Aprovado
"""

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
if m < 5.0:
    print('Reprovado')
elif m > 5.0 and m <= 6.9:
    print('Recuperação')
else:
    print('Aprovado')