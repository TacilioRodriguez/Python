"""
Refaça o Desafio 009, mostranso a tabuata de um numero que
o usuário escolher, só que agora utilizando um laço for.
"""

tabuada = int(input('Digite o numero da tabuada: '))
for t in range(1, 11):
    r = t * tabuada
    print("{} x {} = {}".format(tabuada, t, r))
print('-- FIM --')