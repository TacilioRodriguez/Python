"""Escreva um programa para aprovar emprestimo bancario para a compra de uma casa.
O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar
Calcule o valor da prestação mensal, sabendo que ela nao pode exceder os 30% do salario 
ou então o emprestimo será negado"""

valor = float(input('Qual o valor do Imovel: '))
salario = float(input('Qual o seu salario? R$ '))
ano = int(input('Quantos anos deseja financiar? '))
parcela = valor/(ano*12)
if parcela < salario*0.30:
    print('Emprestimo APROVADO')
else:
    print('Emprestimo NEGADO')