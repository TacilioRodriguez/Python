ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = ((nota1 + nota2) / 2)
    #Nota Composta
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] ')).lower()
    #Caso a resposta seja igual a N ele finaliza o programa
    if resp == 'n':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Media":>8}')
print('-' * 26)
# Para cada item na lista com index, mostre o item na posição correspondente
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')

while True:
    print('-=' * 35)
    opc = int(input('Mostrar nota de qual Aluno? (999 Interrompe) '))
    if opc == 999:
        print('Finalizando ...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')



