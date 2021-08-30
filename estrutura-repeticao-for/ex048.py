"""
Faça um programa que calcule a soma entre todos os numeros impares
que são multiplos de tres e que se encontram no intervalo de 1 até 500
"""
soma = 0
conte = 0
for c in range (1, 501, 2):
    if c %3 == 0:
        conte = conte + 1
        soma = soma + c
print("A soma de todos os {} valores do range são {}".format(conte,soma))