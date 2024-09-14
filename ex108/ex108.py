import moeda

n = float(input('Digite o preço R$: '))
print(f'A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}.')
print(f'O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}.')
print(f'Aumentando {moeda.moeda(n)} em 10% temos {moeda.moeda(moeda.aumentar(n, 10))}.')
print(f'Reduzindo {moeda.moeda(n)} em 13% temos {moeda.moeda(moeda.diminuir(n, 13))}.')
