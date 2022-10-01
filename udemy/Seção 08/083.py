# Você está pintando uma parede.
# As instruções na lata de tinta dizem que **1 lata de tinta pode cobrir 5 metros quadrados** de parede.
# Dada uma altura e largura aleatórias da parede, calcule quantas latas de tinta você precisará comprar.

import math

def calc_pintura(Altura, Largura, Cobertura=5):
    n_latas = (Altura * Largura) / Cobertura
    arredonda_n_latas = math.ceil(n_latas)
    print(f'Voce precisa de {arredonda_n_latas} latas para pintar')

alt = int(input('Digite a Altura: '))
lar = int(input('Digite a Larguda: '))
cobertura = 5
calc_pintura(alt, lar, cobertura)