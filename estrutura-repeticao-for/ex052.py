"""
Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo.
Numero primo - são divisiveis por 1 e por ele mesmo.

"""
n = int(input('Digite um numero: '))
if n % 2 != 0 and n / 1:
    print('É numero Primo')
else:
    print('Não é numero primo')


# Com cores no terminal
num = int(input('Digite um numero: '))
for c in range (1, num +1):
    if num % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    print('{} '.format(c), end=' ')