vlr_hora = 85
dias_uteis = 23
hrs_uteis = 8
vlr_nota = (8*23)*85
print(f'O valor da NF do mês atual é de R$ {vlr_nota:,.2f}')
vlr_nota_anterior = int(input('Digite o valor da NF do mês anterior: R$ '))
vlr_imposto_anterior = vlr_nota_anterior * 0.06
vlr_imposto = vlr_nota * 0.06
vlr_desconto = 400 + vlr_imposto + vlr_imposto_anterior + 2000
print(f'O valor do Imposto de 6% é de R$ {vlr_imposto:.2f}')

saque = vlr_nota - vlr_desconto
print(f'O valor que pode ser sacado é de R$ {saque:,.2f}')