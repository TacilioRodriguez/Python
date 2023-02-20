def fatorial(n, show=False):
    """
    -> Calcula o Fatorial de um numero.
    :param n: O valor a ser calculado
    :param show: Parametro Opcional para mostrar o calculo
    :return: O valor do fatorial de um numero
    """
    resultado = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        resultado *= c
    return resultado


print(fatorial(5, show=False))

