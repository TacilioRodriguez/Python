# frase = 'Curso em Video'
# print(frase[1:13])

'''22 - Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiusculas e minusculas. Quantas letras ao todo
(sem considerar espaços) Quantas letras tem o primeiro nome'''

# nome = str(input('Digite o seu nome: '))
# nmema = nome.upper().strip()
# nmemi = nome.lower().strip()
# nomespa = len(nome.strip())

# print('O nome digitado foi {},\n o nome em Mai é {},\n o nome em Min é {},\n e a qtd de letras sem espaços é {}'.format(nome, nmema, nmemi, nomespa-nome.count(' ')))
# print('Seu primeiro nome tem {}'.format(nome.find(' '))) #mostra somente o primeiro nome digitado

'''23 - Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados
Ex: Digite um numero: 1834:
Unidades: 4
Dezenas: 3
Centena: 8 
Milha: 1 '''

# numero = int(input('Digite um numero de 0 a 9999:'))
# uni = numero //1 % 10 
# dez = numero // 10 % 10
# cen = numero // 100 % 10
# mil = numero // 1000 % 10

# print('Unidade {}, \n Dez {} \n Cen {}, Mil {}'.format(uni, dez, cen, mil))

'''24 - Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome (Santo)'''
# cidade = str(input('Digite o nome da cidade: ')).strip()
# print(cidade[:5].upper == 'SANTO')

# '''25 - Crie um programa que leia o nome de uma pessoa e diga se ela tem (SILVA) no nome'''
# nome = str(input('Digite seu nome: ')).strip()
# print('Tem Silva no nome ? {} '.format('SILVA' in nome.upper()))


'''26 - Faça um programa que leia uma frase pelo teclado e mostre:
Quantas vzs aparece a letra R
Em que posição ela aparece a primeira vez
Em que posição ela aparece a ultima vez'''

# frase = str(input('Digite uma frase: ')).strip().upper()
# print('O R aparece {} vzs \n e a primeira vez é {}, e a ultima vez é {}'.format(frase.count('R'), frase.find('R')+1, frase.rfind('A')+1))

'''27 - Faça um programa que leia o nome completo de uma pessoa, mostrando em seuginda o primeiro e o ultimo
nome separadamente:
Ex: Ana Maria de Souza
Primeiro: Ana
Ultimo: Souza'''

# n = str(input('Digite seu nome completo: ')).strip()
# nome = n.split()
# print ('O seu primeiro nome é {} \n e o ultimo é {}'.format(nome[0], nome[len(nome)-1]))

