from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da Lista: ')
    for i in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.3)


def somapar(lst):
    par = 0
    for n in lst:
        if n % 2 == 0:
            par += n
    print()
    print(f'Somando os valores pares de {lst}, temos {par}.')


numeros = list()
sorteia(numeros)
somapar(numeros)
