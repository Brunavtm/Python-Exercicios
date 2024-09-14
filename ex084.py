lista = list()
dados = list()
mai = men = 0
while True:
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))
    dados.append(nome)
    dados.append(peso)
    if len(lista) == 0:
        mai = men = dados[1]
    else:
        if dados[1] > mai:
            mai = dados[1]
        if dados[1] < men:
            men = dados[1]
    lista.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Ao todo você cadastrou {len(lista)} pessoas.')
print(f'O maior peso foi de {mai} Kg. Peso de ', end='')
for p in lista:
    if p[1] == mai:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi de {men} Kg.', end='')
for p in lista:
    if p[1] == men:
        print(f'[{p[0]}]', end='')
print()


