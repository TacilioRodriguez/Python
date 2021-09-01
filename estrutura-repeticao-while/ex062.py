"""
Melhore o Desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end=' ')
        termo = termo + razao
        cont = cont + 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')