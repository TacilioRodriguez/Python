from time import sleep

def maior(*num):
    print('-='*20)
    print(f'Analisando os valores passados...')
    for n in num:
        sleep(0.3)
        print(f'{n}', end=' ')
    print()
    print(f'No total foram informados {len(num)} ao todo.')
    m = 0
    for i in num:
        if i > m:
            m = i
    print(f'O maior valor informado foi {m}.')


maior(2, 20, 21, 5, 13, 6)
