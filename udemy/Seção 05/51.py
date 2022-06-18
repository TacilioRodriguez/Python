# altura_estudantes = int(input('Digite a altura dos estudantes separadamente: ')).split()
altura_estudantes = [156, 178, 165, 171, 187]
total = 0
qtd_alturas = 0
for n in altura_estudantes:
    total += n
    qtd_alturas += 1

media = total / qtd_alturas
print(f'A lista recebeu {qtd_alturas} valores, e a média é',round(media))
