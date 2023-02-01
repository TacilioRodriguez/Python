def busca(lista, elemento):
    for i in lista:
        if i == elemento:
            print(i)
            return i
    else:
        print('Numero não encontrado')


