def mensagem(msg):
    print('-' * len(msg))
    print(msg)
    print('-' * len(msg))


def area(l, c):
    tamanho = l * c
    print(f'A Area de um terreno {l}x{c} é de {tamanho}m²')


mensagem('Controle de Terrenos')
largura = float(input('Largura (m): '))
cumprimento = float(input('Comprimento (m): '))
area(largura, cumprimento)
