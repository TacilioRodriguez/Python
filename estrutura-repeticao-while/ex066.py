"""
Crie um programa que leia varios numeros inteiros pelo teclado. O programa só vai para quando o usuário digitar
o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles,
desconsiderando a flag.
"""


cont = 0
soma = 0
dig = 0
while dig != 999:
    dig = int(input('Digite um numero: '))
    if dig == 999:
        break
    cont = cont + 1
    soma += dig
print(f'Foram digitados {cont} numeros e a soma é {soma}')
