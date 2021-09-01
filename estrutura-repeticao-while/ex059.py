"""
Crie um programa que leia dois valores e mostre um menu na tela:
    1 Somar
    2 multiplicar
    3 maior
    4 novos numeros
    5 sair do programa

Seu programa deverá realizar a operação solicitada em cada caso
"""
import time 
n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
escolha = 0
while escolha != 5:
    print('-----------------------------------')
    escolha = int(input("""Escolha uma das opções:\n
                [1] Somar
                [2] Multiplicar
                [3] Maior
                [4] Novos numeros
                [5] Sair do programa\n
                Digite ----> """))
    print('-----------------------------------')
    if escolha == 1:
        s = n1 + n2
        print('A soma é {}'.format(s))
    elif escolha == 2:
        s = n1 * n2
        print('O resultado da Multiplicação é {}'.format(s))
    elif escolha == 3:
        if n1 > n2:
            maior = n1
            print('O maior numero é {}'.format(maior))
        else:
            maior = n2
            print('O maior numero é {}'.format(maior))
    elif escolha == 4:
        print('Informe os numeros novamente')
        n1 = int(input('Digite um numero: '))
        n2 = int(input('Digite um numero: '))
    elif escolha == 5:
        print('Finalizando ...')
        time.sleep(2)
        print('OBRIGADO!')
    else:
        print('Opção invalida')
    time.sleep(2)
print('FIM')

