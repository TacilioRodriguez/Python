from random import sample
from time import sleep

print('-' * 30)
print(' ' * 6 + 'JOGO DA MEGA SENA' + ' ' * 6)
print('-' * 30)
qtd_jogos = int(input('Quantos jogos da MEGA SENA quer fazer? '))
tamanho = 6
valores = range(1, 61)
jogos_invidivual = []
jogos = []
print('-=' * 4, f'SORTEANDO OS {qtd_jogos} JOGOS', '-=' * 4)
print()
for i in range(qtd_jogos):
    n = sorted(sample(valores, k=tamanho))
    jogos_invidivual.append(sorted(n))
    sleep(0.8)
    print(f'Jogo {i+1}: {n}')

print('Jogos gerados com sucesso')
