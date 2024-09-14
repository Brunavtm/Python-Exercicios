def metade(preço=0, mostrar=False):
    res = preço / 2
    return res if mostrar is False else moeda(res)


def dobro(preço=0, mostrar=False):
    res = preço * 2
    return res if mostrar is False else moeda(res)


def aumentar(preço=0, taxa=0, mostrar=False):
    res = preço + (preço * taxa / 100)
    return res if mostrar is False else moeda(res)


def diminuir(preço=0, taxa=0, mostrar=False):
        res = preço - (preço * taxa / 100)
        return res if mostrar is False else moeda(res)


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')


def resumo(preço, aum=0, dim=0):
    print(f'_' * 30)
    print('RESUMO DO VALOR'.center(30))
    print(f'_' * 30)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Metade do preço: \t{metade(preço, True)}')
    print(f'Dobro do preço:  \t{dobro(preço, True)}')
    print(f'{aum}% de aumento:  \t{aumentar(preço, aum, True)}')
    print(f'{dim}% de redução:  \t{diminuir(preço, dim, True)}')
    print(f'_' * 30)