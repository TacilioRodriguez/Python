""" Desenvolva uma logica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5:
    Abaixo do peso
- Entre 18.5 a 25:
    Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40:
Obesidade morbida
"""
import time
peso = float(input('Digite o seu peso: '))
print('Aguarde...')
time.sleep(1)
altura = float(input('Digite a altura: '))
print('Aguarde...')
time.sleep(2)
print('Calculando seu IMC...')
time.sleep(2)
imc = peso/(altura**2)
if imc < 18.5:
    print('Abaixo do peso')
elif imc >= 18.5 and imc <= 25:
    print('Peso Ideal')
elif imc > 25 and imc <= 30:
    print('Sobrepeso')
elif imc >= 30 and imc <= 40:
    print('Obesidade')
else:
    print('Obesidade Morbida')