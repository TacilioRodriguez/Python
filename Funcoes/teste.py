
def dobra(lista):
    pos = 0
    while pos < len(lista):
        lista[pos] = lista[pos] * 2
        pos = pos + 1


valores = [2, 4, 6, 8, 10]
dobra(valores)
print(valores)