from random import randint
from time import sleep

def sorteia():
    li = []
    for i in range(1, 6):
        s = randint(1, 10)
        li.append(s)
    # print(li)
    return li


def somaPar(lst):
    print('Sorteando 5 valores da Lista: ')
    for item in lst:
        print(f'{item}', end=' ')
        sleep(0.3)
    par = 0
    for n in lst:
        if n % 2 == 0:
            par += n
    print()
    print(f'Somando os valores pares de {lst}, temos {par}')



sorteia()
somaPar(sorteia())