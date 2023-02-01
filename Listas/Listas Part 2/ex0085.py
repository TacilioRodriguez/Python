l_completa = [[], []]
for i in range(0, 7):
    dig = int(input(f'Digite o {i+1}º numero: '))
    if dig % 2 == 0:
        l_completa[0].append(dig)
    else:
        l_completa[1].append(dig)
print('-=' * 30)
print(f'Os numeros pares são {sorted(l_completa[0])}')
print(f'Os numeros impares são {sorted(l_completa[1])}')
