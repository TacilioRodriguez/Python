"""
Crie um programa que leia uma frase qualquer e diga se ela é um polindromo,
desconsiderando os espaços.
Palindromo - 
Frase que tem o mesmo sentido de tras pra frente.
"""
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1 , -1, -1):
    inverso = inverso + junto[letra]
if inverso == junto:
    print('É um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')
