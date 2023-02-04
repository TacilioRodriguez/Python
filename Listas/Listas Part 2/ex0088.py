from random import sample

qtd_jogos = int(input('Quantos jogos da MEGA SENA quer fazer? '))
tamanho = 6
valores = range(1, 61)
jogos = []
for _ in range(qtd_jogos):
    n = sorted(sample(valores, k=tamanho))
    jogos.append(sorted(n))


print(f'{jogos}', end=' ')
