import moeda

preço = float(input('Digite o preço R$: '))
print(f'{moeda.metade(preço, True)}')
print(f'{moeda.dobro(preço, True)}')
print(f'{moeda.diminuir(preço, 10, False)}')
print(f'{moeda.aumentar(preço, 20, True)}')
