##78
valores = []
maior = []
menor = []
for item in range(0, 5):
    valores.append(int(input(f'Digite um numero para a Posição {item}: ')))
    if item == 0:
        maior = menor = valores[item]
    else:
        if valores[item] > maior:
            maior = valores[item]
        if valores[item] < menor:
            menor = valores[item]

print('=-' * 30)
print(f'Os valores digitados foram {valores}')
print(f'O maior valor foi {maior} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == maior:
        print(f'{indice} | ', end='')
print()
print(f'O menor valor foi {menor} nas posições ', end='')
for indice, valor in enumerate(valores):
    if valor == menor:
        print(f'{indice} | ', end='')

# print(f'O Maior valor foi {max(valores)} e esta na posição {valores.index(max(valores))}')
# print(f'O Menor valor foi {min(valores)} e esta na posição {valores.index(min(valores))}')

##--===============================================---=================================================

##79
numeros = []
while True:
    dig = int(input('Digite um Valor: '))
    if dig in numeros:
        print('Valor Duplicado! Não vou adicionar...')
    else:
        numeros.append(dig)
        print('Valor Adicionado com Sucesso...')

    resp = str(input('Quer continuar? [S/N] ')).lower()
    if resp == 'n':
        break
print('=-' * 30)
print(f'Você digitou os valores {sorted(numeros)}')

##--===============================================---=================================================
##80
from bisect import insort
lista = []
for item in range(5):
    insort(lista, int(input('Digite o número: ')))
    n = int(input('Digite o número: '))
print('=-' * 30)
print(lista)


### ou essa solução

for c in lista:
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1
print('=-' * 30)
print(f'Os valores digitados em ordem foram {lista}')


##--===============================================---=================================================
## 81
resp = 's'
list_num = []
while resp == 's':
    if resp == 's':
        dig = int(input('Digite um numero: '))
        list_num.append(dig)
        resp = str(input('Quer continuar ? [S/N] ')).lower()
    else:
        break

print('-=' * 30)
print(f'Foram digitados {len(list_num)} numeros', sorted(list_num, reverse=True))
if 5 in list_num:
    print('O valor 5 foi digitado')
else:
    print('O valor 5 não foi digitado')

##--===============================================---=================================================

##82
n = []
par = []
impar = []
while True:
    numeros = int(input('Digite um valor: '))
    n.append(numeros)
    cond = str(input('Quer continuar? [s/n] ')).lower()
    if cond == 'n':
        break

for item in n:
    if item % 2 == 0:
        par.append(item)
    else:
        impar.append(item)

print(f'O numeros digitados foram {n}')
print(f'Os numeros pares são {par}')
print(f'Os numeros impares são {impar}')


##--===============================================---=================================================

##83

expres = list(input('Digite uma expressão: '))
if expres.count('(') == expres.count(')'):
    print('Sua expressão é Válida!!')
else:
    print('Sua expressão é Invalida')
