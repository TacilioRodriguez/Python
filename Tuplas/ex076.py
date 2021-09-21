"""
Crie um programa que tenha uma tupla unica com nomes de produtos e seus respectivos preços, na sequencia.
No final, mostre uma listagem de preços, organizando os dados em uma forma tabular.
"""

listagem = ('Lapis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.90,
            'Estojo', 5.75,
            'Mochila', 14.43,
            'Canetas', 4.60,
            'Livro', 34.90)
print('='*30)
print(f'{"LISTAGEM DE PREÇOS":^30}')
print('='*30)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<20}', end=' ')
    else:
        print(f'R${listagem[pos]:>6}')
print('-'*30)
