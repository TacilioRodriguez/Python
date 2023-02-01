temp = []
princ = []
maior_peso = 0
menor_peso = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(int(input('Peso Kg: ')))
    if len(princ) == 0:
        maior_peso = menor_peso = temp[1]
    else:
        if temp[1] > maior_peso:
            maior_peso = temp[1]
        elif temp[1] < menor_peso:
            menor_peso = temp[1]
    resp = str(input('Quer Continuar? [S/N] ')).lower()
    princ.append(temp[:])
    temp.clear()
    if resp == 'n':
        break
print('-=' * 30)

print(f'Foram cadastrados no Total {len(princ)} pessoas')
print(f"O Maior peso foi de {maior_peso}Kg. ", end='')
for pessoa in princ:
    if pessoa[1] == maior_peso:
        print(f'[{pessoa[0]}] ', end='')
print()
print(f"O Menor peso foi de {menor_peso}Kg. ", end='')
for pessoa in princ:
    if pessoa[1] == menor_peso:
        print(f'[{pessoa[0]}] ', end='')