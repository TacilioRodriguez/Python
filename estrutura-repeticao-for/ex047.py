"""
Crie um programa que mostre na tela todos
os numeros pares que estão no intervalo entre 1 e 50.
"""
for par in range(1,50):
    if par % 2 == 0:
        print(par, end=" ")
print('Fim')