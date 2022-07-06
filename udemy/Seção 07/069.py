#Step 1

word_list = ["aardvark", "baboon", "camel"]

from random import choice

palavra_escolhida = choice(word_list)
print(palavra_escolhida)

display = []
for traco in range(len(palavra_escolhida)):
    display.append('_')

palpite = str(input('Adivinhe uma letra ? ')).lower()


for posicao in range(len(palavra_escolhida)):
    letra = palavra_escolhida[posicao]
    if letra == palpite:
        display[posicao] = letra
    else:
        print('ERRADO')

print(display)
