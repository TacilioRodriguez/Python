from time import sleep
# inicio, fim, passo


def contador(inicio=0, fim=0, passo=0):
    #Transformando o Numero em Positivo
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('=-' * 15)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')
    sleep(0.7)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
            sleep(0.2)
        print('FIM!')
        print('=-'*15)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont}', end=' ')
            sleep(0.2)
            cont -= passo
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)

print('=-' * 15)
print('Agora é sua vez de personalizar a contagem: ')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


contador(inicio, fim, passo)