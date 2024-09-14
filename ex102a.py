def factorial(n, show = False):
    """
        Calcula o fatorial de um número.
        :param num: O número a ser calculado.
        :param show: (opcional) mostrar ou não a conta.
        :return: O valor do fatorial de um número n.
        """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


#programa principal
print(factorial(8, True))
help(factorial)