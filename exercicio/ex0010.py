# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-lo,
    # -- sabendo que cada litro de tinta, pinta uma area de 2 m²


largura = int(input('Digite a largura: '))
altura = int(input('Digita a altura: '))
area = largura * altura
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua area é de {} m².'.format(largura, altura, area))
tinta = area/2
print('Para pintar a sua parede voce precisa de {}l de tinta.'.format(tinta))