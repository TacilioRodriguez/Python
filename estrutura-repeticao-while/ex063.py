"""
Escreve um programa que leia um numero n inteiro qualquer e mostre na tela os n primeiros
elementos de uma sequencia de fibonacci.
ex: 0, 1, 1, 2, 3, 5, 8, 13, 21
"""

numero = int(input('Quantos termos deseja visualizar? '))
t1 = 0
t2 = 1
cont = 3
print('{} -> {}'.format(t1, t2), end=' ')
while cont <= numero:
    t3 = t1 + t2
    print('- > {}'.format(t3), end=' ')
    t1 = t2
    t2 = t3
    cont = cont + 1
print('| FIM')