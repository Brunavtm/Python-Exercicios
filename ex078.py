valores = [ ]
for c in range(0, 5):
    valores.append(int(input('Digite um número para posição {}: '.format(c))))
print('Você digitou os valores {}'.format(valores))
print('O menor valor foi {} que apareceu na {} posição.'.format(min(valores), valores.index(min(valores))))
print('O maior valor foi {} que apareceu na {} posição.'.format(max(valores), valores.index(max(valores))))
