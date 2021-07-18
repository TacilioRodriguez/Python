#Faça um algoritmo onde leia o salario do funcionario e mostre com acrescimo de 15%

salario = float(input('Qual o salário do funcionario? R$ '))
porcentagem = float(input('Qual a porcentagem de aumento ? % '))
novosalario = salario + (salario * porcentagem / 100)
print('O salário do funcionario era R${:.2f}, com aumento de {}% o novo salário é de R${:.2f} reais'.format(salario, porcentagem, novosalario))
