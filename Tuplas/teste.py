

nomes = ('Laranja', 'Teto', 'Araraquara')

for item in nomes:
    print(f'\nA palavra {item} tem: ', end=' ')
    for letra in item:
        if letra in 'aeiou':
            print(f'{letra}', end=' ')
