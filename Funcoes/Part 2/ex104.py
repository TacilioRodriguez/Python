def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print('ERRO. Digite um valor inteiro valido.')
    return valor


ne = leiaInt('Digite um numero Valido: ')
print(f'Voce acabou de digitar o numero {ne}')
