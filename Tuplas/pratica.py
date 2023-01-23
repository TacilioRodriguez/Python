# time = ('Palmeiras' ,'Internacional' ,'Fluminense' ,'Corinthians' ,'Flamengo' ,'Athletico-PR'
#         ,'Atlético-MG','Fortaleza' ,'São Paulo' ,'América-MG','Botafogo' ,'Santos' ,'Goiás',
#         'Bragantino','Coritiba','Chapecoence','Ceará','Atletico-GO','Avaí','Juventude')
#
# print(f'Os 5 primeiros colocados são {time[:5]}')
# print(f'Os quatro ultimos colocados são {time[-4:]}')
# print(f'Os times em ordem alfabetica {sorted(time)}')
# print(f'O time da chapecoence esta na posição', time.index('Chapecoence'))


# from random import randint
# numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
# print(f'Os numeros sorteados foram {numeros}')
#
# print(f'Menor valor é {min(numeros)}')
# print(f'Maior valor é {max(numeros)}')


# numero = (int(input('Digite um numero: ')), int(input('Digite outro numero: ')),
#           int(input('Digite mais um numero: ')), int(input('Digite o ultimo numero: ')))
#
# pares = []
# print(f'Você digitou os valores {numero}')
# print(f'O valor 9 apareceu {numero.count(9)} veze(s)')
# if 3 in numero:
#     print('O valor 3 apareceu na ' + f'{numero.index(3)+1}ª' + ' posição')
# else:
#     print('O valor 3 não foi digitado')
#
# for item in numero:
#     if item % 2 == 0:
#         pares.append(item)
# print('Os valores pares foram ', str(pares).strip('[]'))


palavras = ('Laranja', 'Pera', 'Lagarto')

for item in palavras:
    print(f'\nNa palavra {item.upper()} temos: ', end=' ')
    for letra in item:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
