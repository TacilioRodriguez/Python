# import math

# print('Porção Inteira do Numero')
# n = float(input('Digite um Numero qualquer: '))
# print('O numero {} tem a parte inteira de {}'.format(n, math.trunc(n)))

#----------------------------------------------------------------------------------------------------------------

# import math
# print('Calculando a Hipotenusa')
# c1 = float(input('Digite o valor do 1º Cateto Aposto: '))
# c2 = float(input('Digite o valor do 2º Cateto Adjacente: '))
# h = math.hypot(c1,c2) #Utilizando a biblioteca math pra utilizar a função hypot
# print('O calculo dos valores digitados {} e {}, formam a Hipotenusa {:.2f}'.format(c1, c2,h))

#----------------------------------------------------------------------------------------------------------------

# import math
# print('Leitura de um Numero e calcular o seno, cosseno e tangente')
# n = float(input('Digite o valor do Angulo: '))
# c = math.cos(math.radians(n))
# s = math.sin(math.radians(n))
# t = math.tan(math.radians(n))
# print('O valor do angulo é {} \n o Cosseno é {:.2f}\n o Seno é {:.2f} \n Tangente é {:.2f}'.format(n,c,s,t))

#----------------------------------------------------------------------------------------------------------------

# import random
# print('Random de Alunos para apagar Losa')
# print('=================================')
# for aluno in range(0,5):
#     str(input('Digite o nome do aluno: '))
# lista = [aluno]
# escolhido = random.choice(lista)
# print('O Aluno escolhido foi {}'.format(escolhido))

#----------------------------------------------------------------------------------------------------------------

# import random
# n1 = str(input('Digite o aluno: '))
# n2 = str(input('Digite o aluno: '))
# n3 = str(input('Digite o aluno: '))
# n4 = str(input('Digite o aluno: '))
# lista = [n1, n2, n3, n4]
# print('O Aluno escolhido é {}'.format(random.choice(lista)))

#----------------------------------------------------------------------------------------------------------------

import random
n1 = str(input('Digite um nome: '))
n2 = str(input('Digite um nome: '))
n3 = str(input('Digite um nome: '))
n4 = str(input('Digite um nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) #a ordem aleatoria não pode ser utilizado dentro do format
print('A ordem de apresentação é {} '.format(lista))
#print('A ordem de apresentação é {}'.format(random.shuffle(lista)))

import playsound
playsound.playsound('e01.mp3')