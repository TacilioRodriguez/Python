"""
Crie um programa que vai gerar cinco numeros aleatorios e colocar em uma tupla.

Depois disso, mostre a listagem de numeros gerados e também indique o menor e o maior valor que estão na tupla.

"""

from random import sample
aleatorio = sample(range(0,100),5)

print('Os numeros gerados foram = ', aleatorio)
print(f'O menor valor foi {min(aleatorio)}, e o maior valor foi {max(aleatorio)}.')