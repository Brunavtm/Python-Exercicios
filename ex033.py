v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor:'))
lista = [v1, v2, v3]
ordenar = sorted(lista)
print('O menor valor digitado foi {}.'.format(ordenar[0]))
print('O maior valor digitado foi {}.'.format(ordenar[2]))

