#Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
#para salarios superiores a 1250, calcule um aumento de 10%
#para salarios inferiores ou iguais, o aumento é de 15%

salario = float(input('Digite o salario: '))
if salario>1250:
    print('Com o aumento de 10% seu salario será de R${:.2f} reais'.format(salario+(salario*0.1)))
else:
    print('Com o aumento de 15% seu salario será de R${:.2f} reais'.format(salario+(salario*0.15)))
