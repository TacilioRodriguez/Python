"""Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- a vista dinheiro/cheque: 10% de desconto
- em até 2x no cartão: preco normal
- 3x ou mais no cartão: 20% de juros
"""
import time
print('========== Calculando Valores de Um Produto ==========')
valor = float(input('Digite o valor do produto: R$ '))
time.sleep(2)
escolha = print('Escolha a forma de pagamento \n 1 - A Vista (Dinheiro/Cheque) \n 2 - Em 2x no Cartão \n 3 - Em 3x ou mais no cartão.')
print('--------------------------------------')
pgto = int(input('Digite a opção desejada => '))
time.sleep(1)
print('======================================')
print('Processando o valor total a ser pago...')
time.sleep(3)
if pgto == 1:
    vista = valor - (valor*0.10)
    print('O valor a ser pago é de R$ {:.2f}'.format(vista))
elif pgto == 3:
    tres = valor + (valor*0.30)
    print('O valor a ser pago é R$ {:.2f}'.format(tres))
else:
    print('O valor a ser pago é R$ {:.2f}'.format(valor))
