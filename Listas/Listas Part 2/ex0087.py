matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tt_valores = 0
terceira_col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        # Somando os numeros pares da ultima coluna.
        if matriz[l][c] % 2 == 0:
            tt = matriz[l][c]
            tt_valores += tt
    # Somando os numeros da terceira coluna.
    coluna = matriz[l][2]
    terceira_col += coluna


print('-=' * 30)

# Mostrar a estrutura de matriz na saida
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)
print(f'A soma total de valores pares da matriz é {tt_valores}')
print(f'O total da soma dos numeros da ultima coluna é {terceira_col}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')





