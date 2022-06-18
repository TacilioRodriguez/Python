score = [78, 65, 89, 86, 55, 91, 64, 89]
maximo = 0
for numero in score:
    if numero > maximo:
        maximo = numero

print(f'O maior Score é {maximo}')