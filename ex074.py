from random import randint
print('Gerador de 5 números')
numeros = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os números são : {numeros}')
ordem = (sorted(numeros))
print('O menor número gerado é {}.'.format(ordem[0]))
print('O maior número gerado é {}.'.format(ordem[-1]))


