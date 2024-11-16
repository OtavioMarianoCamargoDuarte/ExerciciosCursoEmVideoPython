def fatorial(num, show=False):
    """
    -> A função calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (OPCIONAL) Mostrar ou não o processo de calculo.
    :return: O valor do Fatorial de um número num
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa Principal
print(fatorial(5, show=False))
print(fatorial(8, show=True))
print(fatorial(3))
help(fatorial)
