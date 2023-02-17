from time import sleep

def maior(*num):
    m = 0
    print('-='*20)
    print(f'Analisando os valores passados...')
    for n in num:
        sleep(0.3)
        print(f'{n}', end=' ')
        if m == 0:
            m = n
        else:
            if n > m:
                m = n
    print()
    print(f'No total foram informados {len(num)} valores.')
    print(f'O maior valor informado foi {m}.')


maior(2, 54, 21, 5, 13, 6)
