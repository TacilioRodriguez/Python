n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('Sua média é {:.2f}'.format(m))
if m >= 7:
    print('Voce passou de ano, Parabéns')
else:
    print('Voce foi reprovado, estude mais')