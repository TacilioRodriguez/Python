# Escreva um programa que leia um valor em metros e o exiba convertido em centimentros e melimetros

metro = float(input('Digite o valor em metros: '))
centimetros = float(metro*100)
melimetros = float(metro*1000)
print('O metro é {}, isso é equivalente a {} centimetros e {} melimetros'.format(metro,centimetros,melimetros))