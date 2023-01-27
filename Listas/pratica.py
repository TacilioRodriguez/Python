# valores = [1, 10, 2, 10]
# # for item in range(0, 5):
# #     numeros = int(input('Digite um numero: '))
#
# pos = []
# for x in valores:
#     if valores.count(x) > 1:
#         pos.append(x)
#
# print(pos)
# print(f'O Maior valor foi {max(valores)} e esta na posição {valores.index(max(valores))}')
# print(f'O Menor valor foi {min(valores)} e esta na posição {valores.index(min(valores))}')

# --===============================================---=================================================

# numeros = []
# resp = 's'
# while resp == 's':
#     dig = int(input('Digite um Valore: '))
#     if dig in numeros:
#         print('Valor Duplicado, não vou adicionar...')
#     else:
#         numeros.append(dig)
#         print('Valor Adicionado com Sucesso...')
#
#     resp = str(input('Quer continuar? [S/N] ')).lower()
#
# print(f'Você digitou os valores {sorted(numeros)}')

# --===============================================---=================================================

# from bisect import insort
# lista = []
# for item in range(5):
#     insort(lista, int(input('Digite o número: ')))
# print(lista)

# --===============================================---=================================================
## 81
# resp = 's'
# list_num = []
# while resp == 's':
#     if resp == 's':
#         dig = int(input('Digite um numero: '))
#         list_num.append(dig)
#         resp = str(input('Quer continuar ? [S/N] '))
#
# print(f'Foram digitados {len(list_num)} numeros')
# print(sorted(list_num, reverse=True))
# if 5 in list_num:
#     print('O valor 5 foi digitado')
# else:
#     print('O valor 5 não foi digitado')

# --===============================================---=================================================


##82
# n = []
# par = []
# impar = []
# while True:
#     numeros = int(input('Digite um valor: '))
#     n.append(numeros)
#     cond = str(input('Quer continuar? [s/n] ')).lower()
#     if cond == 'n':
#         break
#
# for item in n:
#     if item % 2 == 0:
#         par.append(item)
#     else:
#         impar.append(item)
#
# print(f'O numeros digitados foram {n}')
# print(f'Os numeros pares são {par}')
# print(f'Os numeros impares são {impar}')


# --===============================================---=================================================

##83

expres = list(input('Digite uma expressão: '))
cont = 0
for item in expres:
    if item == '(':
        cont += 1
    elif item == ')':
        cont += 1

print(cont)
if cont % 2 == 0:
    print('Expressão Valida..')
else:
    print('Expressão Invalida')




































