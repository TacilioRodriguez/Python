# Jogo da Forca

from hangman_words import word_list
from hangman_art import logo, stages
from random import choice


def espaco(qtd):
    print(qtd*'=')


print(logo)
espaco(50)
print('Bem vindo ao jogo da forca, você terá 6 chances para acertar... ')


palavra_escolhida = choice(word_list)
tamanho_palavra = len(palavra_escolhida)
print(f'A Palavra sorteada foi ==>> {palavra_escolhida}')

display = []
for traco in range(tamanho_palavra):
    display.append('_')
# print(display)

lives = 6
game_over = False

# Enquanto game_over for igual a False, faça
while game_over == False:
    espaco(50)
    palpite = str(input('Digite uma Letra: ')).lower()
    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            display[posicao] = letra
    print(display)
    if palpite not in palavra_escolhida:
        lives -= 1
        print(stages[lives])
        if lives == 0:
            game_over = True
            print('Enforcado')
    elif '_' not in display:
        print(f'Você acertou: {display}')
        game_over = True



