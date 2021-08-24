""" Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo se
será formado.
- Equilatero : Todos os lados iguais
- Isosceles : dois lados iguais
- Escaleno: Todos os lados diferentes
"""
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro Segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isosceles')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')
