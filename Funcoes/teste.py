

# def dobra(lista):
#     pos = 0
#     while pos < len(lista):
#         lista[pos] = lista[pos] * 2
#         pos = pos + 1


# valores = [2, 4, 6, 8, 10]
# dobra(valores)
# print(valores)


# Caso 1 
lista  = [500, 1500, 2000, 100, 25]

# Inicializa uma lista vazia
nova_lista = []

#Faz um for na lista, e para cada item multiplica o preço por 2
# for preco in lista:
#     nova_lista. append(preco * 2)
# print(nova_lista)

# Mesmo exemplo acima usando list comprehension
nova_lista_preco = [preco * 2 for preco in lista]
print(nova_lista_preco)