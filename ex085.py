lista = list()
par = list()
impar = list()
for c in range(1, 8):
    valor = (int(input(f'Digite o {c}° valor: ')))
    if valor % 2 == 0:
        par.append(valor)
    if valor % 2 == 1:
        impar.append(valor)
par.sort()
impar.sort()
lista.append(par)
lista.append(impar)
print(f'Os números pares são: {lista[0]}')
print(f'Os números ímpares são: {lista[1]}')


