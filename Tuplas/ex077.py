"""
Crie um programa que tenha uma tupla com varias palavras (não usar acentos). Depois disso, voce deve mostrar,
para cada palavra, quais as suas vogais.
"""

palavras = ('Teste', 'Aliado', 'Uva', 'Musculação', 'Dentista', 'Treino', 'Cobra')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    if letra.lower() not in 'aeiou':
        print(f'Zero Vogais')