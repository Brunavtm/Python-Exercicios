def fatorial(num, show=True):
    """
    Calcula o fatorial de um número.
    :param num: O número a ser calculado.
    :param show: (opcional) mostrar ou não a conta.
    :return: O valor do fatorial de um número n.
    """
    from math import factorial
    fac = factorial(num)
    if show == True:
        print('-' * 30)
        for c in range(num, 0, -1):
            print(f' {c} ', end='')
            if c != 1:
                print('x', end='')
        print(f'= {fac}')
    else:
        print('-' * 30)
        print(f'{fac}')


num = int(input('Digite um número para ver o fatorial: '))
fatorial(num)
