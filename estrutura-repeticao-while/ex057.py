"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Digite o sexo [M/F]: ')).upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor informe seu sexo: ')).upper()
print('Sexo registrado com sucesso!')



# Primeira tentativa, funcionou mas nao como deveria.
# mas = 'M'
# fem = 'F'
# dig = ''
# while (dig != mas) and (dig != fem):
#     dig = str(input('Digite o sexo [M/F]: ')).upper()
#     if dig != mas and dig != fem:
#         dig = print('Digitação incorreta, por favor Digite Novamente')
#     else:
#         print('OK! Obrigado')