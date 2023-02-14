def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


def soma(*num):
    s = 0
    for i in num:
        s += i
    print(s)


valores = [2, 4, 6, 8, 10]
# dobra(valores)
soma(2, 4, 6, 8)
print(valores)
