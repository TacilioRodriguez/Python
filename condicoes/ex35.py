#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo
# o meu foi feito assim
print('-='*20)
print('Analisador de triângulo')
print('-='*20)

a = float(input('Segmento 1: '))
b = float(input('Segmento 2: '))
c = float(input('Segmento 3: '))

if a < b + c and b < a + c and c < b + a:
    print('True')
else:
    print('False')