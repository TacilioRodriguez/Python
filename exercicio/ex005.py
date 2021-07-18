# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

numero = int(input('Digite um numero: '))
dobro = numero*2
triplo = numero*3
raiz = numero ** (1/2)

print('O numero digitado é {}, o dobro {}, triplo {} e raiz quadrada {:.2f}'.format(numero,dobro,triplo,raiz))

