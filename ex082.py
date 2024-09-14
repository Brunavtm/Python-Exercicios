lista = list()
listapar= list()
listaimpar = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
    pos = 0
for c in lista:
    if c % 2 == 0:
        listapar.append(c)
    else:
        listaimpar.append(c)
print('-=' * 30)
print(f'A lista completa é {lista}')
print(f'A lista de números pares é {listapar}')
print(f'A lista de números ímpares é {listaimpar}')
