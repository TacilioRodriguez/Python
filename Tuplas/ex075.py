"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final Mostre:
a) Quantas vezes apareceu o valor 9
b) Em que posição foi digitado o primeiro valor 3
c) Quais foram os numeros pares
"""

num = []
for c in range(0,4):
    num.append(int(input('Digite um numero: ')))
print(num)