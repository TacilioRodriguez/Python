"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final Mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os numeros pares
"""

num = (int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')),
       int(input('Digite um numero: ')))
print(f'O numero 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro numero 3 aparece na posição {num.index(3)+1}')
else:
    print('O valor 3 nao foi digitado')
print('A Tupla digita foi -> ', num)
for n in num:
    if n % 2 == 0:
        print(n, end=' ')

