"""
Crie um programa que tenha uma Tupla totalmente preenchida com uma contagem por extenso,
de zero até vinte.

Seu programa devera ler um numero pelo teclado(entre 0 e 20) e mostra-lo por extenso.
"""
numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

dig = int(input('Digite um numero entre 0 e 20: '))
while dig not in range(0, len(numeros)):
    dig = int(input('Tente novamente. Digite um numero entre 0 e 20: '))
print(f'O Numero digitado foi o', numeros[dig])