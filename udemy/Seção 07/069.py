# Jogo de acertar palavra

#Step 1

word_list = ["ardvark", "baboon", "camel"]
# word_list = ["ta", 'teste']

from random import choice

palavra_escolhida = choice(word_list)
tamanho_palavra = len(palavra_escolhida)
print(palavra_escolhida)

display = []
for traco in range(tamanho_palavra):
    display.append('_')
print(display)


tamanho = 0 #Variavel iteravel/incremental

# Enquanto a quantidade de palpites for menor que o tamanho da palavra e existir espaço vazio na lista
while tamanho < tamanho_palavra and '_' in display:
    palpite = str(input('Digite uma Letra: '))
    for posicao in range(tamanho_palavra):
        letra = palavra_escolhida[posicao]
        if letra == palpite:
            display[posicao] = letra
    tamanho += 1  # incremento da quantidade de palpites
if '_' in display:
    print('Não foi dessa vez')
else:
    print(f'Você acertou: {display}')
