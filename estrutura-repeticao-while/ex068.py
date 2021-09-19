"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
"""

from random import randint

print('======================== JOGO PAR OU IMPAR ========================')
vitoria = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voce jogou {jogador} e o Computador {computador}, no total foi {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Voce VENCEU')
            vitoria += 1
        else:
            print('Voce PERDEU')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Voce VENCEU')
            vitoria += 1
        else:
            print('Voce PERDEU')
            break
    print('Vamos JOGAR novamente...')
print(f'GAME OVER. Voce VENCEU {vitoria}')