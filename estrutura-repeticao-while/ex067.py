"""
Faça um programa que mostre a tabuada de varios numeros, um de cada vez,
para cada valor digitado pelo usuario. O programa será interrompido quando o numero
solicitado for negativo.
"""

while True:
    print('='*35)
    print('           TABUADA        ')
    print('=' * 35)
    dig = int(input('Qual tabuada você quer? '))
    if dig < 0:
        break
    print('~' * 35)
    for c in range(1, 11):
        print(f'{dig} x {c} = {dig*c}')

