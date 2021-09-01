"""
Refaça o Desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
termos da progressao usando a estrutura while
"""

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end=' ')
    termo = termo + razao
    cont = cont + 1
print('FIM')