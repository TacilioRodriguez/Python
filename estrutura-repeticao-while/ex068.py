"""
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
Mostrando o total de vitorias consecutivas que ele conquistou no final do jogo.
"""

def TemLetraU():
    frase = str(input('Digite uma Frase: ')).upper()
    if 'U' in frase:
        print('Tem letra U')
    else:
        print('Não tem Letra U')

TemLetraU()