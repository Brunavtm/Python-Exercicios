def metade(preço=0, mostrar=False):
    if mostrar == True:
        res = moeda(preço / 2)
        return res
    else:
        res = preço / 2
        return res


def dobro(preço=0, mostrar=False):
    if mostrar == True:
        res = moeda(preço * 2)
        return res
    else:
        res = preço * 2
        return res


def aumentar(preço=0, taxa=0, mostrar=False):
    if mostrar == True:
        res = moeda(preço + (preço * taxa / 100))
        return res
    else:
        res = preço + (preço * taxa / 100)
        return res

def diminuir(preço=0, taxa=0, mostrar=False):
    if mostrar == True:
        res = moeda(preço - (preço * taxa/100))
        return res
    else:
        res = preço - (preço * taxa / 100)
        return res


def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.',',')
