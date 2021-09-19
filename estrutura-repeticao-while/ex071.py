"""
Crie um programa que simule o funcionamento de um caixa eletronico. No inicio, pergunte ao
usuario qual será o valor a ser sacado (numero inteiro) e o programa vai informar quantas cedulas
de cada valor serão entregues.
Obs.: Considere que o caixa possui cedulas de R$50, R$20, R$10 e R$1
"""

print('========================= ITAU =========================')

sacar = int(input('Qual voce quer sacar? '))
total = sacar
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} notas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('===== VOLTE SEMPRE =====')

