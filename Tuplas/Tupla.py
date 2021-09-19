# Maneiras de se utilizar Tuplas

# Utlilizando o range e len para imprimir as posições.
print('========= Utilizando Range e Len =========')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
for comida in range(0, len(lanche)):
    print(lanche[comida])
print('Comi demais')



# Jeito mais simples e comum
print(' ')
print('========= Jeito Simples =========')
for comida in lanche:
    print(f'Eu Comi {comida}')


# Forma de utilizar o enumarate e duas variaveis no For.
print(' ')
print('========= Usando o Enumerate =========')
for pos, comida in enumerate(lanche):
    print(f'Eu comi {comida}, e esta na posição {pos}')

# Organizando a tupla
print(sorted(lanche))

# Count com Index na tupla

c = (1,2,3,4,5,6)
print(c.index(2))