# Desenvolva um programa que leia as duas notas de um aluno, calcule o mostre a sua média

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
soma = nota1 + nota2
média = soma/2
print('A soma das duas notas é {:.2f}, sua média ficou em {:.2f}'.format(soma,média))