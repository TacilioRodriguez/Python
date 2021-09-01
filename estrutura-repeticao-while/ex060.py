"""
Faça um programa que leia um numero qualquer e mostre o seu fatorial.
ex: 5! = 5*4*3*2*1=120
"""

# Fazer com while e com for

n = int(input('Digite um numero: '))
c = n
f = 1
print('Calculando {} fatorial'.format(n))
while c > 0:
    print('{} '.format(c), end=' ')
    print('x ' if c > 1 else ' = ', end=' ')
    f = f * c
    c = c - 1 
print('{}'.format(f))


# Mesmo desafio utilizando o FOR
num = int(input('Digite um numero: '))
f = 1
c = num
for t in range(num, 0, -1):
    print('{} '.format(t), end=' ')
    f = f * c
    c = c - 1
print('{}'.format(f))
