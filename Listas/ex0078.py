


lanche = ['teste1', 'teste2', 'teste3']

lanche[2] = 'picole'
print(lanche[2])

lanche.append('coockie') #adicionar o item a lista
lanche.insert(0,'dog')  #adicionar em qualquer posição da lista
print(lanche)

# Apagar elementos da lista

del lanche[3]
lanche.pop(3)
lanche.remove('dog')
