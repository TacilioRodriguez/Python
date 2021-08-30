"""
Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas
daques que forem pares. Se o valor digitado for impar, desconsidere-o.
"""
soma = 0
for n in range (0, 6):
    numero = int(input('Digite um numero: '))
    if numero %2 == 0:
        soma = soma + numero
print(soma)
print('FIM')